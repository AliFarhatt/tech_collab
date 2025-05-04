try:
    import re
    import os
    import json
    import glob
    import fitz     # PyMuPDF
    import base64
    import logging
    import chromadb

    from utils.prompts import *
    from utils.gemini_api import *
except Exception as e:
    logging.error("Error loading modules in main.py: ", str(e))


# Preprocessing resume tools
def extract_text_from_pdf(file_name='this_resume.pdf'):
    try:
        try:
            # Open the PDF file
            pdf_document = fitz.open(file_name)
            print("Aliiiiuuu")
        except Exception as e:
            print(str(e))
            print('File opened failed: ', file_name)
        # Initialize an empty list to store the text from each page
        pages_text = []
        
        # Iterate over each page
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            page_text = page.get_text("text")
            pages_text.append(page_text)
        
        page_0_text = pages_text[0]
        try:
            page_1_text = pages_text[1].page_content
            try:
                page_2_text = pages_text[2].page_content
                return page_0_text + " \n " + page_1_text + " \n " + page_2_text
            except:
                return page_0_text + " \n " + page_1_text
        except:
                return page_0_text
    except Exception as e:
        print("Error In extract_text_from_pdf function: ", str(e))
        return None
   
def save_b64_as_pdf(base64_pdf, output_filename='this_resume.pdf'):
    try:
        # Decode the base64 string
        pdf_data = base64.b64decode(base64_pdf)
        # Write the decoded data to a file
        with open(output_filename, 'wb') as file:
            file.write(pdf_data)
        print(f"PDF saved as {output_filename}")
        return output_filename
    except Exception as e:
        print("Error In save_b64_as_pdf function: ", str(e))
        return None

def write_and_read_json(json_string, file_name='temp.txt'):
    # Write the JSON string to a text file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(json_string)
    
    # Read the JSON string back from the text file
    with open(file_name, 'r', encoding='utf-8') as file:
        read_json_string = file.read()
    json_data = json.loads(read_json_string)
    return json_data

def clean_json_string1(json_string):
    # Remove leading and trailing whitespace
    json_string = json_string.strip()
    json_string = json_string.replace('`', '')
    json_string = json_string.replace('json', '')
    json_string = json_string.replace('JSON', '')
    json_string = json_string.replace('\"', '"')
    # json_string = json_string.replace("\'", '"')

    json_string = json_string.replace('*', '')
    json_string = json_string.replace('#', '')
    # Replace problematic characters
    json_string = json_string.replace("\\n", "\n").replace("\\", "")
    
    # Fix any misplaced commas at the end of lists or objects
    json_string = re.sub(r",\s*(\]|\})", r"\1", json_string)
    json_string = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_string)

    # Fix any misplaced commas at the end of lists or objects
    json_string = re.sub(r",\s*(\]|\})", r"\1", json_string)

    # Add missing commas between items
    json_string = re.sub(r'("\w+":\s*{[^{}]*}\s*){2,}', lambda m: re.sub(r'}\s*{', '}, {', m.group(0)), json_string)
    
    json_string = write_and_read_json(json_string)
    return json_string

def clean_json_string(json_string):
    # Remove leading and trailing whitespace
    json_string = json_string.strip()
    # Remove any unnecessary keywords or characters
    json_string = json_string.replace('`', '')
    json_string = json_string.replace('json', '')
    json_string = json_string.replace('JSON', '')
    json_string = json_string.replace('*', '')
    json_string = json_string.replace('#', '')
    json_string = json_string.replace('\"', '"')
    # json_string = json_string.replace("\'", '"')
    # Replace problematic characters
    json_string = json_string.replace("\\n", "\n")
    # Don't remove backslashes entirely; keep them for escaping characters
    json_string = json_string.replace("\\", "")

    # Fix any misplaced commas at the end of lists or objects
    json_string = re.sub(r",\s*(\]|\})", r"\1", json_string)

    # Remove non-printable characters
    json_string = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_string)

    # Ensure commas are placed correctly between objects
    json_string = re.sub(r'("\w+":\s*{[^{}]*}\s*){2,}', lambda m: re.sub(r'}\s*{', '}, {', m.group(0)), json_string)
    json_string = write_and_read_json(json_string)

    return json_string

import json

import re

def preprocess_pdf(file_name='this_resume.pdf'):
    try:
        resume_text = extract_text_from_pdf(file_name)
        
        if not resume_text or len(resume_text.strip()) == 0:
            print(f"No text extracted from PDF: {file_name}")
            return None, None

        resume_json = LLM_structure_resume(resume_text)

        if not resume_json or not isinstance(resume_json, str):
            print(f"LLM did not return a valid response for file: {file_name}")
            return None, resume_text

        print("=== Raw LLM Resume JSON ===")
        print(resume_json)
        print("===========================")

        # Handle case if server sent HTML instead of JSON
        if "<!DOCTYPE html" in resume_json.lower() or "<html" in resume_json.lower():
            print("Received HTML instead of JSON. Likely LLM server error.")
            return None, resume_text

        # Handle Markdown formatting with triple backticks
        if resume_json.strip().startswith("```"):
            print("Detected Markdown formatting. Cleaning it...")
            # Remove triple backticks and optional 'json'
            resume_json = re.sub(r'^```(?:json)?\s*', '', resume_json.strip(), flags=re.IGNORECASE)
            resume_json = re.sub(r'\s*```$', '', resume_json.strip())

        # Double check if after cleaning, it is a valid JSON object
        if not resume_json.strip().startswith("{") or not resume_json.strip().endswith("}"):
            print("LLM output is not a complete JSON object. Skipping.")
            return None, resume_text

        try:
            resume_json_clean = clean_json_string1(resume_json)
        except Exception as e:
            print(f"Failed to clean JSON response for file: {file_name}")
            print('Error:', str(e))
            return None, resume_text

        return resume_json_clean, resume_text

    except Exception as e:
        print(f'Failed to process resume file: {file_name}')
        print('Error in preprocess_pdf function in utils.py:', str(e))
        return None, None

# Vector Database tools
# def initialize_projects_DB(projects_ai, 
#                            projects_security, 
#                            projects_android, 
#                            projects_imageProcessing, 
#                         #    projects_web,
#                            projects_cloud,
#                            projects_raspberrypi,
#                            projects_ml,
#                            projects_iot,
#                            projects_gps_gsm):
#     # embedding = sentence_transformers.encode([text])
#     # collection.add(
#         # embeddings=embedding,...)
    
#     persistentClient = chromadb.PersistentClient(path=r"C:\Users\abede\OneDrive\Desktop\aboudi\LU\Semester10-FYP\code\utils\vector_db")
#     collection = persistentClient.get_or_create_collection(name="projects_collection",
#                                         metadata={"hnsw:space": "cosine"} , # l2 is the default
#                                         embedding_function=embedding_function)
        
#     all_projects = projects_ai + \
#                     projects_security + \
#                     projects_android + \
#                     projects_imageProcessing + \
#                     projects_cloud+ \
#                     projects_raspberrypi + \
#                     projects_ml + \
#                     projects_iot + \
#                     projects_gps_gsm
#                     # projects_web+ 

#     # Create corresponding unique IDs and metadata
#     all_ids = [f"ai_{i}" for i in range(len(projects_ai))] + \
#             [f"sec_{i}" for i in range(len(projects_security))] + \
#             [f"and_{i}" for i in range(len(projects_android))] + \
#             [f"img_{i}" for i in range(len(projects_imageProcessing))] + \
#             [f"cloud_{i}" for i in range(len(projects_cloud))] + \
#             [f"rasp_{i}" for i in range(len(projects_raspberrypi))] + \
#             [f"ml_{i}" for i in range(len(projects_ml))] + \
#             [f"iot_{i}" for i in range(len(projects_iot))] + \
#             [f"gpsgsm_{i}" for i in range(len(projects_gps_gsm))]
#             # [f"web_{i}" for i in range(len(projects_web))] + \

#     all_metadata = [{"category": "AI"}] * len(projects_ai) + \
#                 [{"category": "Security"}] * len(projects_security) + \
#                 [{"category": "Android"}] * len(projects_android) + \
#                 [{"category": "Image Processing"}] * len(projects_imageProcessing) + \
#                 [{"category": "Cloud"}] * len(projects_cloud) + \
#                 [{"category": "RaspberryPi"}] * len(projects_raspberrypi) + \
#                 [{"category": "ML"}] * len(projects_ml) + \
#                 [{"category": "IoT"}] * len(projects_iot) + \
#                 [{"category": "GPS GSM"}] * len(projects_gps_gsm) 
#                 # [{"category": "Web"}] * len(projects_web) + \
#     print(type(all_projects))
#     print(type(all_projects[0]))
#     print(len(all_projects))
#     # print(all_projects)
#     # Add the flattened list to the collection
#     collection.add(
#         documents=all_projects,
#         ids=all_ids,
#         metadatas=all_metadata,
#     )
#     return collection

def query_projects_DB(student_text, n_results, collection, preferences_list=None):
    try:
        if preferences_list is None:
            results = collection.query(
                query_texts=[student_text], # Chroma will embed this for you
                n_results=n_results # how many results to return
            )
            return results['ids'], results["documents"]
        elif preferences_list:
            # Build the query filter based on the given preferences
            query_filter = {"category": {"$in": preferences_list}}
            
            # Execute the query
            results = collection.query(
                query_texts=[student_text], # Chroma will embed this for you
                n_results=n_results,
                where=query_filter
            )
            
            return  results['ids'], results["documents"]
    except Exception as e:
        print("Error in query_projects_DB function in utils.py: " + str(e))
        return None, None

def retrieve_projects(collection, projects_IDs):
    try:
        projects_json_list = []
        for i,project_ID in enumerate(projects_IDs):
            result = collection.get(ids=project_ID)
            project_json = result['documents'][0]
            # Extract the project's text from the result
            if result['ids']:
                # print('project_'+i+' retrieved')
                projects_json_list.append(project_json) 
            else:
                print(f'No project with ID: {project_ID} was found')
        return projects_json_list
    except Exception as e:
        print("Error in get_projects_by_ids function in utils.py: " + str(e))
        return None

def save_projects_in_text_file(projects_json_list, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for i,project_json in enumerate(projects_json_list):
                try:
                    # project_json = clean_json_string(project_json)
                    project_json = json.loads(project_json)
                    for project_subject in project_json: 
                        file.write(str(project_json[project_subject]) + ', ')
                except Exception as e:
                    print(e)
                    print("failed to process project: ", i)
                file.write('\n') 
    except Exception as e:
        print("Error in save_projects_in_text_file: ", e)
        
def add_projects_toDB(projects_file_path, category, distance_metric='cosine', vector_db_path=r"C:\Users\abede\OneDrive\Desktop\aboudi\LU\Semester10-FYP\code\utils\vector_db"):
    try:
        persistentClient = chromadb.PersistentClient(path=vector_db_path)
        if distance_metric == 'cosine':
            collection = persistentClient.get_or_create_collection(name="projects_collection",
                                                metadata={"hnsw:space": "cosine"} , # l2 is the default
                                                embedding_function=embedding_function)
        # elif distance_metric == 'dot_product':
        #     collection = persistentClient.get_or_create_collection(name="projects_collection",
        #                                         metadata={"hnsw:space": "dot"} , # l2 is the default
        #                                         embedding_function=embedding_function)
        
        else:
            collection = persistentClient.get_or_create_collection(name="projects_collection",
                                                embedding_function=embedding_function)

        projects_list = get_projects_list(projects_file_path)
        
        # Create corresponding unique IDs and metadata
        count = collection.count()
        ids = [f"{category}_{i}" for i in range(count, count + len(projects_list))]

        for i,project in enumerate(projects_list):
            print('started projects adding')
            collection.add(
                documents=[project],
                ids=ids[i : i + 1],
                metadatas=[{"category": category}]
            )
            print(f"Project {i} added to DB")

        print(f'{category} Projects added successfully')
    except Exception as e:
        print(f'{category} Projects added failed')
        print("Error in add_projects_toDB function in utils.py: " + str(e))

def get_projects_list(file_path):
    json_list = []
    with open(file_path, 'r') as file:
        data = file.read()
    # Parse the entire content as a JSON array
    parsed_data = json.loads(data)

    # Convert each dictionary in the list back to a JSON string
    json_list = [json.dumps(item) for item in parsed_data]

    return json_list

def load_projects(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
                list_of_dicts = json.load(file)
        return list_of_dicts
    except Exception as e:
        print(e)
        return None
    
def retrieve_all_categories(collection):
    try:
        # Get all documents from the collection
        results = collection.get()  # Retrieves all documents

        categories = set()  # Using a set to avoid duplicates

        # Loop through documents and extract categories
        for document in results['documents']:
            if isinstance(document, str):
                document = json.loads(document)

            # Check if 'category' field exists
            if 'category' in document:
                category_field = document['category']

                # Add the exact category as it appears (even if it contains commas)
                if isinstance(category_field, str):
                    categories.add(category_field.strip())

        # Convert the set back to a list and return it
        return list(categories)

    except Exception as e:
        logging.error("Error in retrieve_exact_used_categories: " + str(e))
        return None
    
def retrieve_projects_by_category(collection, category, start_index=0, chunk_size=24):
    try:
        # Retrieve projects filtered by the exact category using an exact match query
        query = {"category": category}  # Exact match
        results = collection.get(where=query)
        
        projects_json_list = results['documents']

        # Return the projects in chunks (pagination)
        return projects_json_list[start_index:start_index + chunk_size]
    except Exception as e:
        logging.error("Error in retrieve_projects_by_category: " + str(e))
        return None

def retrieve_projects_all_categories(collection, start_index=0, chunk_size=24):
    try:
        # Retrieve projects from all categories with pagination
        results = collection.get()  # Retrieve all documents
        projects_json_list = results['documents']
        return projects_json_list[start_index:start_index + chunk_size]
    except Exception as e:
        logging.error("Error in retrieve_projects_all_categories: " + str(e))
        return None
    
def retrieve_projects_by_category2(collection, category, n_results=10):
    try:
        # projects_IDs = []
        # for j in range(n_results):
        #     projects_IDs.append(f'{category}_{j}')
        # projects_json_list = []
        # for i,project_ID in enumerate(projects_IDs):
        #     result = collection.get(ids=project_ID)
        #     # Extract the project's text from the result
        #     if result['ids']:
        #         print('project_'+str(i)+' retrieved')
        #         projects_json_list.append(result['documents'][0]) 
        #     else:
        #         print(f'No project with ID: {project_ID} was found')
        results = collection.get(where={'category': category})
        projects_json_list = results['documents']
        return projects_json_list[:n_results]
    except Exception as e:
        print("Error in get_projects_by_ids function in utils.py: " + str(e))
        return None

def recommend_project(preference, approach, resume_text=''):
    try:
        if approach == 2:
            if preference=="":
                LLM_response = LLM_prompt_3(resume_text)
            else:
                LLM_response = LLM_prompt_4(resume_text, preference)
        elif approach == 1:
            LLM_response = LLM_prompt_6(preference)
        return LLM_response  # Convert to JSON string
    except Exception as e:
        print("Error In recommend function: ", str(e))
        return None

def initialize_students_DB(resumes_folder_path, embedding_function):
    persistentClient = chromadb.PersistentClient(path="vector_db_2")
    students_collection = persistentClient.get_or_create_collection(name="students_collection",
                                        metadata={"hnsw:space": "cosine"}, # l2 is the default
                                        embedding_function=embedding_function)
    
    pdf_files = glob.glob(os.path.join(resumes_folder_path, '*.pdf'))
    resumes_json_list = []
    resumes_text_list = []
    for i,file_name in enumerate(pdf_files):
        resume_json, resume_text = preprocess_pdf(file_name=file_name)
        resumes_json_list.append(resume_json)
        resumes_text_list.append(resume_text)
        print(i)

    save_resumes_in_text_file(resumes_text_list, file_path='resumes_text.txt')
    save_resumes_in_text_file(resumes_json_list, file_path='resumes_json.txt')
    
    # Create corresponding unique IDs and metadata
    all_ids = [str(i) for i in range(len(resumes_json_list))]

    # Add the flattened list to the collection
    students_collection.add(
        documents=resumes_json_list,
        ids=all_ids
        # metadatas=all_metadata,
    )
    return students_collection

def get_resume_by_id(collection, student_ID):
    try:
        # print(collection.count())
        # print(collection.get())
        result = collection.get(ids=[f'{str(student_ID)}'])
        # print(type(result))
        if result['ids']:
            resume_json = result['documents'][0]
            print(f'Resume of student with ID= {student_ID} was retrieved')
            return resume_json
        else:
            print(f'No student with ID: {student_ID} was found')
            return None
    except Exception as e:
        print("Error in get_resume_by_id function in utils.py: " + str(e))
        return None

def query_students_DB(collection, resume_text, n_results):
    try:
        results = collection.query(
            query_texts=[resume_text], # Chroma will embed this for you
            n_results=n_results # how many results to return
        )
        return results['ids'], results["documents"]

    except Exception as e:
        print("Error in query_students_DB function in utils.py: " + str(e))

def save_resumes_in_text_file(resumes_json_list, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        for i,resume_json in enumerate(resumes_json_list):
            try:
                # resume_json = clean_json_string(resume_json)
                resume_json = json.loads(resume_json)
                for resume_subject in resume_json: 
                    if resume_subject != 'contact':
                        file.write(str(resume_json[resume_subject]) + ', ')
            except Exception as e:
                print("failed to process resume ", i)
                print("Error in save_resumes_in_text_file: " + str(e))
            file.write('\n') 


