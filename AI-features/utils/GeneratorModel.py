try:
    import tqdm
    import json
    import chromadb
    from typing import List
    
    from utils.prompts import *
    from utils.gemini_api import *
    import google.generativeai as genai
    from chromadb.utils import embedding_functions
except Exception as e:
    print("Error in importing libraries in GeneratorModel.py: %s" % e)


class GeneratorModel:
    def __init__(self):
        try:
            self.model = genai.GenerativeModel("gemini-2.0-flash", generation_config={"response_mime_type": "application/json"})
            google_api_key = 'AIzaSyCxHZzWgfpgT91e-ReTrqioroVenes4Ato'
            genai.configure(api_key=google_api_key)

            # This will automatically load any previously saved collections.
            persist_directory_projects = r'data/vector_db'
            persist_directory_students = r'data/vector_db_2'
            self.client_projects = chromadb.PersistentClient(path=persist_directory_projects)
            self.client_students = chromadb.PersistentClient(path=persist_directory_students)

            # create embedding function
            self.embedding_function = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
                api_key=google_api_key, task_type="RETRIEVAL_QUERY"
            )
            # self.query = "Given this CV choose 10 suitable tech projects based on his experience: "
            self.projects_collection = self.client_projects.get_or_create_collection( 
                name='projects_collection', 
                embedding_function=self.embedding_function,
                metadata={"hnsw:space": "cosine"} # l2 is the default
            )
            self.students_collection = self.client_students.get_or_create_collection(
                name='students_collection',
                embedding_function=self.embedding_function,
                metadata={"hnsw:space": "cosine"} # l2 is the default
            )
        except Exception as e:
            print("Error in __init__ of GenerateModel class: %s" % e)    

    def build_prompt(self, context: List[str], resume_text, preference='') -> str:
        """
        Args:
        context (List[str]): The context of the query, returned by embedding search.

        Returns:
        A prompt for the LLM (str).
        """
        # combine the prompts to output a single prompt string
        system_response = f"{LLM_prompt_RAG(resume_text, preference, context)}"

        return system_response

    def match_S2P_RAG(self, resume_text) -> None:
        """
        S2P: Student to Projects matching function
        This function takes a resume_text and/or student_ID
        returns a list of Projects(IDs) matching his profile.
        """
        try:
            # Query the collection to get the 8 most relevant results
            results = self.projects_collection.query(
                query_texts=[resume_text], n_results=8, include=["documents", "metadatas"]
            )

            # Get the response from Gemini
            #response = self.build_prompt(results["documents"], resume_text, '')  
            return query_texts
        except Exception as e:
            print('Failed to match student to projects. ')
            print(f'Error in function match_S2S_RAG: {e}')
            return None

    def match_S2S(self, resume_text, number_similar=8) -> None:
        """
        S2S: Student to Students matching function
        This function takes a resume_text
        returns a list of student_IDs matching his profile.
        """
        try:
            # Query the collection to get the 5 most relevant results
            # print('resume: ')
            # print(type(resume_text))
            # resume_dict = json.dumps(resume_text)
            # query_text = resume_dict['summary'] + resume_dict['skills']
            # print(resume_text)
            # print(type(resume_text))
            results = self.students_collection.query(
                query_texts=resume_text, n_results=number_similar, include=["documents", "metadatas"]
            )

            # print(type(results))
            # print('################################')
            # print(results)
            # print('################################')
            # we should return the IDs of the students
            return results["ids"][0][1:]  # [1:] to exclude the given student himself
        except Exception as e:
            print('Failed to match student to students')
            print(f'Error in function match_S2S: {e}')
            return [None]
        # typically results is as follows:
        # results = 
        # {'ids': [['web_57',
            # 'web_152',
            # 'web_133',
            # 'web_150',
            # 'web_91',
            # 'web_46',
            # 'web_156',
            # 'web_64',
            # 'web_113',
            # 'web_0']],
        # 'distances': [[0.45868009328842163,
            # 0.48265910148620605,
            # 0.4933401942253113,
            # 0.502886950969696,
            # 0.5092998147010803,
            # 0.5116475820541382,
            # 0.5156773924827576,
            # 0.5172253251075745,
            # 0.532210111618042,
            # 0.5353328585624695]],
        # 'metadatas': [[{'category': 'Web'},
            # {'category': 'Web'},
            # {'category': 'Web'},
            # {'category': 'Web'},
            # {'category': 'Web'},
            # {'category': 'Web'},
            # {'category': 'Web'},
            # {'category': 'Web'},
            # {'category': 'Web'},
            # {'category': 'Web'}]],
        # 'embeddings': None,
        # 'documents': [['Food Ordering System: An application for ordering food online from restaurants and food vendors.',
            # 'eCommerce Online Shopping using PHP: An e-commerce platform for online shopping.',
            # 'Online Book Store: Ecommerce using PHP: An e-commerce platform for buying and selling books online.',
            # 'Medical Shop using PHP Online Pharmacy Management System: An online pharmacy management system.',
            # 'eCommerce Old Book Store Shopping with eWallet using PHP: An eCommerce platform for buying and selling old books with eWallet integration.',
            # 'Inventory Management System: A system for tracking and managing inventory levels, orders, and supplies.',
            # 'eRestaurant Online Shopping For Food: An online platform for ordering food from restaurants.',
            # 'Garments Management System Using PHP: A system for managing inventory, orders, and sales in the garment industry.',
            # 'Online SMART BUSINESS - 1 Retailer 2) Distributor 3) Stockiest: A platform to manage interactions between retailers, distributors, and stockists.',
            # 'E-commerce website: Develop a fully functional online shopping website with features like user registration, product catalogue, shopping cart, and payment gateway integration.']],
        # 'uris': None,
        # 'data': None,
        # 'included': ['metadatas', 'documents', 'distances']
            # }

    def add_student_to_DB(self, resume_dict):
        try:
            student_ID = self.students_collection.count() + 1
            resume_json = json.dumps(resume_dict)
            self.students_collection.add(documents=[resume_json], 
                                        ids=[str(student_ID)])
                                        #  metadatas=new_metadatas,
            print(f'New student added to vector database successfully with ID: {student_ID}')
            return student_ID
        except Exception as e:
            print('Failed to add student to vector database')
            print(f'Error in function add_student_to_DB: {e}')
            return None

    def add_projects_to_DB(self, new_projects_list):
        count = self.projects_collection.count()
        print(f"Collection already contains {count} documents")
        ids = [str(i) for i in range(count, count + len(new_projects_list))]

        # Load the documents in batches of 100
        for i in tqdm(
            range(0, len(new_projects_list), 100), desc="Adding documents", unit_scale=100
        ):
            self.projects_collections_collection.add(
                ids=ids[i : i + 100],
                documents=new_projects_list[i : i + 100],
                metadatas=metadatas[i : i + 100],  # type: ignore
            )

        new_count = self.projects_collection.count()
        print(f"Added {new_count - count} projects")



