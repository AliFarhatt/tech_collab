<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Models\User;
use App\Models\StudentData;
use App\Models\Skill;
use App\Models\UserProject;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;
use Tymon\JWTAuth\Facades\JWTAuth;
use Illuminate\Support\Facades\Mail;
use Illuminate\Support\Str;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Facades\Http; 

class AuthController extends Controller
{
    public function register(Request $request)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8',
        ]);
    
        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
            'email_verified' => true,
            'registration_completed' => false,
        ]);
    
        $verificationToken = JWTAuth::fromUser($user);
    
        // Generate the verification link
        $verificationLink = env('FRONTEND_URL') . '/verify-email?token=' . $verificationToken;
    
        try {
            Mail::send('emails.verify', ['user' => $user, 'token' => $verificationToken], function ($message) use ($user) {
                $message->to($user->email);
                $message->subject('Verify your email address');
            });
        } catch (\Exception $e) {
            // Log the error, but don't interrupt the registration process
            \Log::error('Failed to send verification email: ' . $e->getMessage());
        }
        
    
        return response()->json([
            'message' => 'User registered successfully. Please check your email for verification.',
            'status' => true,
            'verification_link' => $verificationLink, 
        ], 201);
    }    

    public function verifyEmail(Request $request)
    {
        try {
            // Retrieve the token from the request body
            $token = $request->input('token');
    
            if (!$token) {
                return response()->json(['message' => 'Token not provided.'], 400);
            }
    
            // Authenticate the user using the token
            $user = JWTAuth::setToken($token)->authenticate();
    
            if (!$user) {
                return response()->json(['message' => 'Invalid token or user not found.'], 400);
            }
    
            // Mark the user's email as verified
            $user->email_verified = true;
            $user->save();
    
            // Generate a new token for the user
            $newToken = JWTAuth::fromUser($user);
    
            // Return the new token, user object, and status
            return response()->json([
                'message' => 'Email verified successfully.',
                'status' => true,
                'token' => $newToken,
                'user' => $user,
            ]);
        } catch (\Exception $e) {
            return response()->json(['message' => 'Token is invalid or expired.'], 400);
        }
    }      

   public function login(Request $request)
    {
        $credentials = $request->only('email', 'password');

        if (!$token = JWTAuth::attempt($credentials)) {
            return response()->json(['message' => 'Invalid credentials'], 401);
        }

        $user = JWTAuth::user();

        $verificationToken = JWTAuth::fromUser($user);

        if (!$user->email_verified) {
            Mail::send('emails.verify', ['user' => $user, 'token' => $verificationToken], function ($message) use ($user) {
                $message->to($user->email);
                $message->subject('Verify your email address');
            });
            return response()->json(['message' => 'Your email is not verified yet. Kindly check your inbox'], 403);
        }

        return response()->json([
            'status' => true,
            'token' => $token,
            'user' => $user,
        ]);
    }

    public function logout()
    {
        Auth::logout();
        return response()->json(['message' => 'Successfully logged out', 'status' => true]);
    }

    public function me()
    {
        return response()->json(Auth::user());
    }

    public function refreshToken(Request $request)
    {
        try {
            // Retrieve the token from the Authorization header
            $currentToken = JWTAuth::getToken();
    
            if (!$currentToken) {
                return response()->json(['message' => 'Token not provided.'], 400);
            }
    
            // Refresh the token
            $newToken = JWTAuth::refresh($currentToken);
    
            // Retrieve the authenticated user with the related data
            $user = JWTAuth::setToken($newToken)->authenticate();
    
            if (!$user) {
                return response()->json(['message' => 'User not found.'], 404);
            }
    
            // Eager load the relationships: skills, following, followers, and userProjects
            $user->load('skills', 'following', 'followers', 'userProjects');
    
            // Return the new token and user object with the loaded relations
            return response()->json([
                'message' => 'Token refreshed successfully.',
                'status' => true,
                'token' => $newToken,
                'user' => $user,
            ]);
        } catch (\Tymon\JWTAuth\Exceptions\TokenInvalidException $e) {
            return response()->json(['message' => 'Token is invalid.'], 401);
        } catch (\Tymon\JWTAuth\Exceptions\JWTException $e) {
            return response()->json(['message' => 'Could not refresh token.'], 500);
        }
    }
    

    public function completeRegistration(Request $request)
    {
        // Validate the incoming request data
        $request->validate([
            'bio' => 'nullable|string',
            'general_field' => 'nullable|string',
            'linkedin_profile' => 'nullable|string',
            'skills' => 'nullable|array',
            'skills.*' => 'string',
            'projects' => 'nullable|array',
            'projects.*.name' => 'required|string',
            'projects.*.description' => 'nullable|string',
        ]);
    
        // Get the authenticated user
        $user = Auth::user();
    
        // Update the user's information directly in the users table
        $user->update([
            'bio' => $request->input('bio'),
            'general_field' => $request->input('general_field'),
            'linkedin_profile' => $request->input('linkedin_profile'),
            'profile_picture' => $user->profile_picture, 
            'vector_id' => $user->vector_id, 
        ]);
    
        // Handle the skills
        if ($request->has('skills')) {
            // Remove existing skills
            Skill::where('user_id', $user->id)->delete();
            
            // Add new skills
            foreach ($request->input('skills') as $skillName) {
                $user->skills()->create(['skill' => $skillName]);
            }
        }
        if ($request->has('projects')) {
  
            foreach ($request->input('projects') as $project) {
            // Optional debug log
            Log::info('Creating project:', $project);
    
            $user->userProjects()->create([
            'user_id' => Auth::id(), // Get the authenticated user's ID
            'title' => $project['name'],
            'description' => $project['description'] ?? null,
            'status' => $project['status'] ?? null,
            'url' => $project['url'] ?? null,
            'technologies' => implode(', ', $project['technologies'] ?? []), // Convert array to string
            'start_date' => $project['start_date'] ?? null,
            'end_date' => $project['end_date'] ?? null,
        ]);
        }
        }
        $user->registration_completed = true;
        $user->save();

        $user->load('skills');
        $user->load('userProjects');
        $user->load('following');
        $user->load('followers');
    
        return response()->json([
            'message' => 'User information completed successfully.',
            'status' => true,
            'user' => $user,
        ]);
    }   
    
    public function getCvAsBase64()
    {
        // Get the authenticated user
        $user = Auth::user();
    
        // Ensure the user has a CV
        if (!$user->cv) {
            return response()->json([
                'message' => 'No CV found for this user.',
                'status' => false
            ], 404);
        }
    
        // Get the file path from the user's cv column
        $filePath = $user->cv;
    
        // Check if the file exists in storage
        if (!Storage::disk('public')->exists($filePath)) {
            return response()->json([
                'message' => 'CV file not found.',
                'status' => false
            ], 404);
        }
    
        // Get the contents of the file
        $fileContent = Storage::disk('public')->get($filePath);
    
        // Convert the file contents to base64
        $base64Cv = base64_encode($fileContent);
    
        return response()->json([
            'data' => $base64Cv,
            'status' => true
        ], 200);
    }

    public function uploadCV(Request $request)
    {
        // Validate the incoming request data
        $request->validate([
            'cv' => 'nullable|file|mimes:pdf|max:5120',
        ]);
    
        // Get the authenticated user
        $user = Auth::user();
    
        // Handle the CV file upload and convert to base64
        if ($request->hasFile('cv')) {
            // Store the CV in the public disk
            $cvPath = $request->file('cv')->store('cvs', 'public');
            $cvContent = Storage::disk('public')->get($cvPath); // Get the file content
            $cvBase64 = base64_encode($cvContent); // Convert the file content to base64
    
            // Prepare form data for API request
            $formData = [
                'pdf_b64' => $cvBase64,
            ];
    
            // Send request to the external AI API to add the student to the database
            $apiResponse = Http::asMultipart()->post(env('AI_API') . '/add_Student_To_DB', $formData);
    
            // Check if the API call was successful
            if ($apiResponse->failed()) {
                // Delete the uploaded CV if the API call fails
                Storage::disk('public')->delete($cvPath);
    
                return response()->json([
                    'message' => 'Error calling AI API.',
                    'status' => false,
                    'data' => $cvBase64
                ], 500);
            }
    
            // Decode the API response
            $apiData = $apiResponse->json();
    
            // Check if a student_ID is returned
            if (!isset($apiData['student_ID'])) {
                // Delete the uploaded CV if the API call fails to return student_ID
                Storage::disk('public')->delete($cvPath);
    
                return response()->json([
                    'message' => 'Failed to get student ID from AI API.',
                    'status' => false,
                ], 400);
            }
    
            // Update the user's CV and vector_id (from student_ID) in the database
            $user->cv = $cvPath;
            $user->vector_id = (string)$apiData['student_ID'];
            $user->save();
    
            // Optional: If the API response contains skills, update them
            if (isset($apiData['skills']) && is_array($apiData['skills'])) {
                // Remove existing skills
                Skill::where('user_id', $user->id)->delete();
    
                // Add new skills
                foreach ($apiData['skills'] as $skillName) {
                    $user->skills()->create(['skill' => $skillName]);
                }
            }
            if (isset($apiData['projects']) && is_array($apiData['projects'])) {
                foreach ($apiData['projects'] as $project) {
                $user->userProjects()->create([
                'title' => $project['name'],                          // required
                'description' => $project['description'] ?? null,
                'status' => null,
                'url' => null,
                'technologies' =>  null,
                'start_date' => null,
                'end_date' =>  null,
            ]);
            }
            }
            // Return success response
            return response()->json([
                'message' => 'User registration completed successfully with AI data.',
                'status' => true,
                'user' => $user,
                'data' => $apiData
            ]);
        }
    
        // If no CV is uploaded, return an error
        return response()->json([
            'message' => 'CV is required for registration.',
            'status' => false,
        ], 400);
    }
}
