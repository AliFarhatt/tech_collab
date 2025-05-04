<?php
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::group(['middleware' => 'api', 'prefix' => 'auth'], function ($router) {
    Route::post('register', [AuthController::class, 'register']);
    Route::post('login', [AuthController::class, 'login']);
    Route::post('verify', [AuthController::class, 'verifyEmail']);
    Route::post('logout', [AuthController::class, 'logout']);
    Route::post('refresh', [AuthController::class, 'refreshToken']);
});

Route::group([
    'middleware' => ['auth:api'],
    'prefix' => 'v1'

], function ($router) {
    Route::post('upload-cv', [AuthController::class, 'uploadCV']);
    Route::post('complete-registration', [AuthController::class, 'completeRegistration']);

    // Project session routes
    Route::post('project-sessions', [ProjectSessionController::class, 'createSession']); 
    Route::get('project-sessions', [ProjectSessionController::class, 'getUserProjectSessions']); 
    Route::get('project-sessions/{sessionId}', [ProjectSessionController::class, 'getSessionData']);

    // Project routes
    Route::post('project-sessions/{sessionId}/projects', [ProjectController::class, 'createProject']); 
    Route::post('projects', [ProjectController::class, 'createStandaloneProject']); 
    Route::post('projects/{projectId}/bookmark', [ProjectController::class, 'toggleBookmark']);
    Route::get('projects/bookmarked', [ProjectController::class, 'getBookmarkedProjects']);
    Route::get('projects/standalone', [ProjectController::class, 'getStandaloneProjects']);

    Route::get('user/cv-base64', [AuthController::class, 'getCvAsBase64']);

    Route::post('user/follow', [UserController::class, 'follow']);
    Route::post('user/unfollow', [UserController::class, 'unfollow']);
    Route::get('users/search', [UserController::class, 'searchUsers']);
    Route::get('user/{id}', [UserController::class, 'getUserById']);
    Route::patch('user/skills', [UserController::class, 'updateSkills']);
    Route::post('user/project', [UserController::class, 'addUserProject']);
    Route::patch('/user/project/{id}', [ProjectController::class, 'updateUserProject']);
    Route::post('users/get-by-vector-ids', [UserController::class, 'getUsersByVectorIds']);

    Route::post('projects/collection/get-by-category', [ProjectCollectionController::class, 'getPaginatedProjects']);
    Route::get('projects/collection/categories', [ProjectCollectionController::class, 'getAllCategories']);
});
