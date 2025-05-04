try:
    import random
    import uvicorn
    import logging

    from utils.utils import *
    from utils.prompts import *
    from utils.GeneratorModel import *
    from pydantic import BaseModel

    from fastapi import FastAPI, File, Form, HTTPException
    from fastapi.responses import JSONResponse
    from fastapi.middleware.cors import CORSMiddleware
except Exception as e:
    logging.error(f"Error loading modules: {e}")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load the vector db
GeneratorModel_1 = GeneratorModel()
# tested successfully
@app.post("/recommend_project_1")
async def recommend_project_1(student_ID: int = Form(),
                            preference: str = Form()):
    """
    This API recommends a project based on CV and preferences list; using Semantic search on between student's profile and projects Database
    Input:  - student_ID integer
            # - Resume PDF base64 encoded
            - List of fields preferences
    Output: JSON string
    """
    try:  
        resume_json = get_resume_by_id(GeneratorModel_1.students_collection, student_ID)
        # pdf_path = save_b64_as_pdf(pdf_b64)
        # resume_text = extract_text_from_pdf(pdf_path)
        resume_dict = json.loads(resume_json)
        resume_text = resume_dict['skills']
        student_text = str(resume_text) + "\n" + preference
        projects_IDs, projects_text = query_projects_DB(student_text, 20, GeneratorModel_1.projects_collection)
        #print(projects_text[0])
        # print(type(projects_text[0]))
        project_titles = []
        recommended_projects = []
        for project in projects_text[0]:
            project = json.loads(project)
            if project['title'] not in project_titles and len(project_titles)<10:
                project_titles.append(project['title'])
                recommended_projects.append(project)
                print(project['title'])
        return JSONResponse(content=recommended_projects, status_code=200)

    except Exception as e:
        logging.error('In main.py: %s', str(e))
        return JSONResponse(content={'error': str(e)}, status_code=500)

# tested successfully
@app.post("/recommend_project_2")
async def recommend_project_2(student_ID: int = Form()):
    """
    This API recommends a project based on CV and preferences list; using RAG on our projects Database, given student ID or resume
    Input:  - Resume PDF base64 encoded
            - List of fields preferences
    Output: JSON string
    """
    try:
        resume_json = get_resume_by_id(GeneratorModel_1.students_collection, student_ID)
        recommended_project = GeneratorModel_1.match_S2P_RAG(resume_json)
        recommended_project = clean_json_string1(recommended_project)
        # If clean_json_string1 returns a string, convert it to a dictionary
        if isinstance(recommended_project, str):
            recommended_project = json.loads(recommended_project)
    
        return JSONResponse(content=recommended_project, status_code=200)

    except Exception as e:
        logging.error('In recommend_project_2 in main.py: %s', str(e))
        return JSONResponse(content={'error': str(e)}, status_code=500)

# problem with parsing json response of resumes [skipped succefully for now]
# tested successfully
@app.post("/Match_S2S")
async def Match_S2S(student_ID):
    """
    This API recommends a project based on CV and preferences list; using RAG on our projects Database, given student ID or resume
    Input:  
        - student ID 
    Output: JSON string:
        - list of string of student IDs
    """
    try:
        # assert isinstance(student_ID, str) , "Preference must be a string"
        # assert isinstance(str(student_ID), int) , "Student ID must be an integer"

        students_IDs = []
        resume_text = get_resume_by_id(GeneratorModel_1.students_collection, str(student_ID))
        # print(resume_text)
        resume_text = json.loads(resume_text)
        resume_skills = resume_text['skills']
        # resume_skills_summary = resume_skills + [resume_text['summary']]
        students_IDs = GeneratorModel_1.match_S2S(resume_skills, number_similar=30)
        for i in ['27','37','38', '46', '63', '69', '73', '82']:
            if i in students_IDs:
                students_IDs.remove(i)
        # print(students_IDs)
        # students_IDs = GeneratorModel_1.match_S2S(resume_skills_summary)
        # students_IDs = GeneratorModel_1.match_S2S(resume_text)
        similar_skills = []
        for ID in students_IDs:
            resume_text = get_resume_by_id(GeneratorModel_1.students_collection, str(ID))
            resume_text = json.loads(resume_text)
            similar_skills.append(resume_text['skills'])
        
        # print('Resume skills: ')
        # print(resume_skills)
        # print("Similar skills: ")
        # print(similar_skills)
        similar_10_IDs = random.sample(students_IDs, 10)
        return JSONResponse(content=similar_10_IDs, status_code=200)

    except Exception as e:
        logging.error('In main.py: %s', str(e))
        return JSONResponse(content={'error': str(e)}, status_code=500)

# tested successfully
@app.post("/add_Student_To_DB")
async def Add_student_to_DB(pdf_b64: str = Form()):
    """
    This API recommends a project based on CV and preferences list; using RAG on our projects Database, given student ID or resume
    Input:  - Resume PDF base64 encoded
    Output: JSON string
            - student ID 
    """
    try:
        pdf_path = save_b64_as_pdf(pdf_b64)
        resume_json, resume_text = preprocess_pdf(pdf_path)

        # Check if resume_json was processed correctly
        if resume_json is None:
            raise ValueError("Failed to process resume JSON from the uploaded PDF.")

        student_ID = GeneratorModel_1.add_student_to_DB(resume_json)

        skills = resume_json.get('skills', [])  
        summary = resume_json.get('summary', "")  

        response_data = {
            "student_ID": student_ID,
            "skills": skills,
            "summary": summary
        }
        return JSONResponse(content=response_data, status_code=200)

    except Exception as e:
        print("Failed to add New Student")
        logging.error('In Add_student_to_DB function in main.py: %s', str(e))
        return JSONResponse(content={'error': str(e)}, status_code=500)
async def delete_student_from_DB(student_id: str):
    """
    This API deletes a student from the vector database given their student ID.
    Input: student_id (string)
    Output: Success or failure message
    """
    try:
        # Assuming the `GeneratorModel_1.students_collection` has a method to delete an entry by ID
        result = GeneratorModel_1.students_collection.delete(student_id)
        
        if result:  # Assuming the result is True if the deletion was successful
            return JSONResponse(content={"message": f"Student {student_id} deleted successfully"}, status_code=200)
        else:
            return JSONResponse(content={"error": f"Student {student_id} not found or could not be deleted"}, status_code=404)

    except Exception as e:
        logging.error('In delete_student_from_DB function: %s', str(e))
        return JSONResponse(content={'error': str(e)}, status_code=500)

@app.get("/retrieve_categories")
async def retrieve_categories():
    """
    This API retrieves all unique project categories from the database.
    Output: JSON string with a list of categories
    """
    try:
        # Retrieve distinct categories from the database
        categories = retrieve_all_categories(GeneratorModel_1.projects_collection)

        if categories:
            return JSONResponse(content={"categories": categories}, status_code=200)
        else:
            return JSONResponse(content={"message": "No categories found."}, status_code=404)

    except Exception as e:
        logging.error('In retrieve_categories function: %s', str(e))
        return JSONResponse(content={'Error': str(e)}, status_code=500)
    
import json
from fastapi import HTTPException

@app.post("/retrieve_projects_by_category")
async def retrieve_projects_by_category(category: str, page: int = 1):
    """
    This API retrieves projects filtered by the given category.
    It supports infinite loading with each chunk containing 24 projects.
    Input:  - category: The category to filter by (e.g., AI, Android, Cloud).
            - page: The current page number (for pagination).
    Output: JSON string with the list of filtered projects and the total count
    """
    try:
        # Normalize the category for case-insensitive matching
        normalized_category = category.strip().lower()

        # Pagination: Calculate the starting index based on the page number
        chunk_size = 24
        start_index = (page - 1) * chunk_size

        # Retrieve all projects from the collection
        results = GeneratorModel_1.projects_collection.get()

        # Check if results['documents'] is a list
        if not isinstance(results['documents'], list):
            raise HTTPException(status_code=500, detail="Invalid structure in project data")

        # Deserialize projects and filter by the exact category
        projects = []
        for project in results['documents']:
            # Check if the project is a string (and needs to be parsed) or a dictionary
            if isinstance(project, str):
                project = json.loads(project)  # Convert string to dictionary

            # Ensure the project is a dictionary and contains 'category'
            if isinstance(project, dict) and 'category' in project:
                project_category = project['category']

                # If category is a list, check if the given category exists in the list
                if isinstance(project_category, list):
                    project_category_list = [cat.strip().lower() for cat in project_category]
                    if normalized_category in project_category_list:
                        projects.append(project)

                # If category is a string, normalize and compare directly
                elif isinstance(project_category, str):
                    if project_category.strip().lower() == normalized_category:
                        projects.append(project)

        # Get the total count of filtered projects
        total_projects = len(projects)

        # Return the filtered projects in chunks (pagination)
        filtered_projects = projects[start_index:start_index + chunk_size]

        if not filtered_projects:
            raise HTTPException(status_code=404, detail="No projects found for the given category")

        return JSONResponse(content={"total": total_projects, "projects": filtered_projects, "page": page}, status_code=200)

    except Exception as e:
        logging.error('Error in retrieve_projects_by_category function: %s', str(e))
        return JSONResponse(content={'Error': str(e)}, status_code=500)

class RetrieveProjectsByCategoriesRequest(BaseModel):
    categories: List[str]
    page: int = 1

@app.post("/retrieve_projects_by_categories")
async def retrieve_projects_by_categories(request: RetrieveProjectsByCategoriesRequest):
    """
    This API retrieves projects filtered by the given categories.
    It supports infinite loading with each chunk containing 24 projects.
    Input:  - categories: List of categories to filter by (e.g., AI, Android, Cloud).
            - page: The current page number (for pagination).
    Output: JSON string with the list of filtered projects and the total count
    """
    try:
        # Normalize the categories for case-insensitive matching
        normalized_categories = [category.strip().lower() for category in request.categories]
        page = request.page

        # Pagination: Calculate the starting index based on the page number
        chunk_size = 24
        start_index = (page - 1) * chunk_size

        # Retrieve all projects from the collection
        results = GeneratorModel_1.projects_collection.get()

        # Check if results['documents'] is a list
        if not isinstance(results['documents'], list):
            raise HTTPException(status_code=500, detail="Invalid structure in project data")

        # Deserialize projects and filter by the given categories
        projects = []
        for project in results['documents']:
            # Check if the project is a string (and needs to be parsed) or a dictionary
            if isinstance(project, str):
                project = json.loads(project)  # Convert string to dictionary

            # Ensure the project is a dictionary and contains 'category'
            if isinstance(project, dict) and 'category' in project:
                project_category = project['category']

                # If category is a list, check if any of the given categories exist in the list
                if isinstance(project_category, list):
                    project_category_list = [cat.strip().lower() for cat in project_category]
                    if any(cat in project_category_list for cat in normalized_categories):
                        projects.append(project)

                # If category is a string, normalize and compare to any of the given categories
                elif isinstance(project_category, str):
                    if project_category.strip().lower() in normalized_categories:
                        projects.append(project)

        # Get the total count of filtered projects
        total_projects = len(projects)

        # Return the filtered projects in chunks (pagination)
        filtered_projects = projects[start_index:start_index + chunk_size]

        if not filtered_projects:
            raise HTTPException(status_code=404, detail="No projects found for the given categories")

        return JSONResponse(content={"total": total_projects, "projects": filtered_projects, "page": page}, status_code=200)

    except Exception as e:
        logging.error('Error in retrieve_projects_by_categories function: %s', str(e))
        return JSONResponse(content={'Error': str(e)}, status_code=500)


class RetrieveProjectsRequest(BaseModel):
    category: str
    page: int = 1  # Default page is 1

@app.post("/retrieve_projects")
async def retrieve_projects(request: RetrieveProjectsRequest):
    """
    This API retrieves a list of projects based on the given category from the database.
    It supports infinite loading with each chunk containing 24 projects.
    Input:  - category: AI, Android, Cloud, or "all" for all categories.
            - page: The current page number (for pagination).
    Output: JSON string
    """
    try:
        category = request.category
        page = request.page

        assert isinstance(category, str), "category must be a string"

        # Pagination: Calculate the starting index based on the page number
        chunk_size = 24
        start_index = (page - 1) * chunk_size

        if category.lower() == "all":
            # Load projects from all categories with infinite loading
            projects_json = retrieve_projects_all_categories(GeneratorModel_1.projects_collection, start_index, chunk_size)
        else:
            # Load projects from a specific category
            projects_json = retrieve_projects_by_category(GeneratorModel_1.projects_collection, category, start_index, chunk_size)

        recommended_projects = [json.loads(project) for project in projects_json]

        return JSONResponse(content={"projects": recommended_projects, "page": page}, status_code=200)

    except Exception as e:
        logging.error('In retrieve_projects function in main.py: %s', str(e))
        return JSONResponse(content={'Error': str(e)}, status_code=500)
    
@app.get("/retrieve_all_projects")
async def retrieve_all_projects():
    """
    This API retrieves all projects and their total count from the database.
    Output: JSON string with the list of projects and the total count
    """
    try:
        # Retrieve all projects from the collection
        results = GeneratorModel_1.projects_collection.get()

        # Get the list of projects
        projects = results['documents']

        # Ensure each project is deserialized from stringified JSON
        deserialized_projects = [json.loads(project) if isinstance(project, str) else project for project in projects]

        # Calculate the total number of projects
        total_projects = len(deserialized_projects)

        # Return the deserialized projects and their total count
        return JSONResponse(content={"total": total_projects, "projects": deserialized_projects}, status_code=200)

    except Exception as e:
        logging.error('In retrieve_all_projects function: %s', str(e))
        return JSONResponse(content={'Error': str(e)}, status_code=500)
                             
@app.post("/generate_project_1")
async def generate_project_1(preference: str = Form()):
    """
    This API takes a list of preferences from the user and generates a project.
    Input: JSON string of preferences
    Output: JSON string
    """

    try:
        assert isinstance(preference, str) , "Preference must be a JSON string"
        
        generated_project = recommend_project(preference, approach=1)
        # print(generated_project)
        generated_project = clean_json_string(generated_project)
        print()
        # print('after cleaning: ')
        # print(generated_project)
        return JSONResponse(content=generated_project, status_code=200)
    except Exception as e:
        logging.error('In main.py: %s', str(e))
        return JSONResponse(content={'error': str(e)}, status_code=500)

# tested successfully
@app.post("/generate_project_2")
async def generate_project_2(student_ID: int = Form(),
                        preference: str = Form()):
    """
    This API takes a list of preferences from the user and generates a project.
    Input:  - Resume PDF base64 encoded
            - List of fields preferences
    Output: JSON string
    """
    try:
        assert isinstance(preference, str) , "Preference must be a string"
        
        # pdf_path = save_b64_as_pdf(pdf_b64)
        resume_json = get_resume_by_id(GeneratorModel_1.students_collection, student_ID)
        # resume_text = extract_text_from_pdf(pdf_path)
        generated_project = recommend_project(preference, approach=2, resume_text=resume_json)
        generated_project = clean_json_string(generated_project)
        if isinstance(generated_project, str):
            recommended_project = json.loads(generated_project)
        return JSONResponse(content=generated_project, status_code=200)
        # return generated_project

    except Exception as e:
        logging.error('In main.py: %s', str(e))
        return JSONResponse(content={'error': str(e)}, status_code=500)


@app.post("/retrieve_studentsDB")
async def retrieve_studentsDB():
    """
    This API returns a list of JSON strings of all students Database.
    Output: JSON string
    """
    try:
        ids = GeneratorModel_1.students_collection.get()['ids']
        docs = GeneratorModel_1.students_collection.get()['documents']
        students_db_json_list = []
        for id,doc in zip(ids, docs):
            if id not in ['27','37','38', '46', '63', '69', '73', '82']:
                dict_doc = json.loads(doc)
                dict_doc['ID'] = id
                students_db_json_list.append(dict_doc)
        return JSONResponse(content=students_db_json_list, status_code=200)

    except Exception as e:
        logging.error('In main.py: %s', str(e))
        return JSONResponse(content={'error': str(e)}, status_code=500)


if __name__ == "__main__":
    # uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT")))
    uvicorn.run(app, host='0.0.0.0', port=8001)