from utils.gemini_api import *
# from gemini_api import *
import random

#LLM prompts

def LLM_prompt(resume_text):

    prompt = f"""
        Given a resume text of a student. Your task is to do the following:

        - Recommend a suitable project for this student based on his Experience, Skills and summary in the given resume text below.

        The project should include Name, Description, Steps, Requirements, Tips.
        The resume_text is delimited with triple backticks.
        The recommended project should be realistic for his academic level, after your suggestion review the project again.

        Make your JSON format response as follows:
        {{
            "Project_Name": "Project name specifically chosen",
            "Project_Description": "Clear description of the project",
            "Project_Steps": "List of technical steps for building version 0",
            "Project_Requirements": "Required knowledge in specific tools/areas, Data, ",
            "Project_Tips": "Tips needed for the process of "
        }}

        Resume Text: '''{resume_text}'''
        """
    return get_completion(prompt)
#not used
def LLM_prompt_2(resume_text):

    prompt = f"""
        Given a resume text of a student. Your task is to do the following:

        - Recommend a suitable project for this student based on his Previoues projects, Experience, Skills and Summary in the given resume text below.

        The project should include Name, Description, Steps, Requirements, Tips and Applications.
        The project could be related to 1 of the expertise only.
        The resume_text is delimited with triple backticks.
        The recommended project should be suitable for his academic level, after your suggestion review the project again.

        Make your JSON format response as follows:
        {{
            "Project_Name": "Project name specifically chosen",
            "Project_Description": "Clear description of the project",
            "Project_Steps": "List of technical steps for building version 0",
            "Project_Requirements": "Required knowledge in specific tools/areas, Data, ",
            "Project_Tips": "Tips that accelerates the process"
            "Project_Applications": "Applications to apply this project in real life"

        }}

        Resume Text: '''{resume_text}'''
        """
    return get_completion(prompt)

def LLM_prompt_3(resume_text):
    prompt = f"""
    You are an expert career advisor specializing in technology and engineering fields. Given the resume text of a student, your task is to recommend a suitable project based on their experience, skills, and summary provided in the resume.

    The recommended project should be:
    - Develop a project that is unique and innovative, clearly differing from any of the student's previous work.
    - Designed to enhance and expand the student's knowledge and abilities, pushing their boundaries to explore new areas.
    - Resourceful: suggest links, techniques, text book references and examples in the steps and tips.

    Provide your recommendation in the following JSON format:
    {{
        "Project_Name": "A concise, descriptive name for the project",
        "Project_Description": "A detailed description of the project, including its objectives and relevance to the student's background",
        "Project_Steps": [
            "A list of clear, actionable steps to build the project (version 0)"
        ],
        "Project_Requirements": [
            "A list of required knowledge, tools, and resources needed for the project"
        ],
        "Project_Tips": [
            "Helpful tips and best practices for successfully completing the project"
        ],
        "Project_Applications": ["Applications to apply this project in real life"]
    }}

    Review the project to ensure it is feasible and beneficial for the student's academic and professional development, and ensure that it is not a mere repetition of their previous work.

    Resume Text: '''{resume_text}'''
    """
    return get_completion(prompt)

def LLM_prompt_4(resume_text, preference):
    prompt = f"""
    You are an expert career advisor specializing in technology and engineering fields. 
    Given the resume text of a student, and his preferences, your task is to recommend a suitable project based on their Preference field, experience, skills, and summary provided in the resume.
    The recommended project should be:
    - Develop a project that is unique and innovative, clearly different from any of the student's previous work.
    - Designed to enhance and expand the student's knowledge and abilities, pushing their boundaries to explore new areas.
    - Resourceful: suggest links, techniques, text book references and examples in the steps and tips.

    Provide your recommendation in the following JSON format:
    {{
        "Project_Name": "A concise, descriptive name for the project",
        "Project_Description": "A detailed description of the project, including its objectives and relevance to the student's background",
        "Project_Steps": [
            "A list of clear, actionable steps to build the project (version 0)"
        ],
        "Project_Requirements": [
            "A list of required knowledge, tools, and resources needed for the project"
        ],
        "Project_Tips": [
            "Helpful tips and best practices for successfully completing the project"
        ],
        "Project_Applications": ["Applications to apply this project in real life"]
    }}

    Review the project to ensure it is feasible and beneficial for the student's academic and professional development, and ensure that it is not a mere repetition of their previous work.

    Resume Text: '''{resume_text}'''
    Preferences: '''{preference}'''
    """
    return get_completion(prompt)
#not used
def LLM_prompt_5(preferences):

    prompt = f"""
        Given a list of preferneces of a tech student. Your task is to do the following:

        - Recommend a suitable project for this student based on the preference given below.

        The project should include Name, Description, Steps, Requirements, Tips.
        The resume_text is delimited with triple backticks.
        The recommended project should be realistic for his academic level, after your suggestion review the project again.

        Make your JSON format response as follows:
        {{
        "Project_Name": "A concise, descriptive name for the project",
        "Project_Description": "A detailed description of the project, including its objectives and relevance to the student's background",
        "Project_Steps": [
            "A list of clear, actionable steps to build the project (version 0)"
        ],
        "Project_Requirements": [
            "A list of required knowledge, tools, and resources needed for the project"
        ],
        "Project_Tips": [
            "Helpful tips and best practices for successfully completing the project"
        ],
        "Project_Applications": ["Applications to apply this project in real life"]
        }}


        preference: '''{preferences}'''
        """
    temperature = random.random()
    print(f"Temperature: {temperature}")
    return get_completion(prompt, temp = temperature)

def LLM_prompt_6(preferences, temperature=1):

    prompt = f"""
        Given a JSON string of preferences of a tech student that includes: focus_area, complexity_level, tools_and_technologies, duration, team_size, expected_outcome.
        Recommend a suitable project for the student.
        The project should be tailored to their interests only.
        
        Your task is to provide:

        - A project name that is concise and descriptive.
        - A detailed description of the project, explaining its objectives, relevance to the student's background, and expected outcomes.
        - A series of actionable steps to develop the project from start to finish.
        - A list of necessary knowledge, tools, and resources needed to successfully complete the project.
        - Practical tips and best practices for effectively carrying out the project.
        - List of Potential real-world applications or extensions of the project.

        Format your response as a JSON object with the following structure:
        {{
        "Project_Name": "A concise, descriptive name for the project",
        "Project_Description": "A detailed description of the project, including its objectives and relevance to the student's background",
        "Project_Steps": [
            "A list of clear, actionable steps to build the project (version 0)"
        ],
        "Project_Requirements": [
            "A list of required knowledge, tools, and resources needed for the project"
        ],
        "Project_Tips": [
            "Helpful tips and best practices for successfully completing the project"
        ],
        "Project_Applications": ["Applications to apply this project in real life"]
        }}

        The student's preference list: '''{preferences}'''
        """
    temperature = random.random()
    print(f"Temperature: {temperature}")
    return get_completion(prompt, temp = temperature)

def LLM_structure_resume(resume_text):
    prompt = f'''
            You are given raw CV data. Please extract and structure the following information into a JSON format:

            1. Summary: A brief overview or summary of the individual's background. if not found, write a brief summary based on his background.
            2. Education: Extract the degree name from the education section.
            3. Skills: List the skills mentioned in the CV.
            4. Work Experience: For each work experience entry, include:
                - Role: The job title or role.
                - Summary: A brief description of the role or key responsibilities.
            5. Certifications: List the certifications mentioned in the CV.
            6. Projects: For each project, include:
                - Name: The name of the project.
                - Description: A brief description of the project.

            Dont add any other fields from the CV.
            Incase no summary found, generate a summary according to his other info.
            Output the structured information in JSON format exactly as this:

            {{
            "summary": "Summary of the resume_text individual's background.",
            "education": [    {{      "degree": "Degree Name"    }}  ],
            "skills": [    "Skill 1",    "Skill 2"  ],
            "work_experience": [    {{      "role": "Job Title",      "summary": "Brief description of the role or key responsibilities."    }}  ],
            "certifications": [    "Certification 1",    "Certification 2"  ],
            "projects": [    {{      "name": "Project Name",      "description": "Brief description of the project."    }}  ]
            }}

            Given resume {resume_text}
            '''
    return get_completion(prompt)


def LLM_recommend_tips(resume_text):
    prompt = f"""
    You are an expert career advisor specializing in technology and engineering fields.
    Given the resume text of a student, your task is to provide personalized learning and growth tips based on their Preference field, experience, skills, and summary provided in the resume.

    The tips should:
    - Encourage the student to explore new areas and push their boundaries beyond their current knowledge.
    - Be resourceful: suggest relevant links, techniques, textbook references, and examples to support the student's learning.
    - Be practical and actionable, offering clear steps or strategies the student can implement to improve their skills and knowledge.
    - Be tailored to the student's background, ensuring they build on their existing strengths while addressing any gaps.

    Provide your recommendations in the following JSON format:
    {{
        "Learning_Goals": ["A concise list of areas the student should focus on to enhance their skills and knowledge"],
        "Growth_Strategies": [
            "Actionable strategies or steps the student can take to achieve their learning goals"
        ],
        "Resource_Suggestions": [
            "Links, books, tutorials, or courses that will aid the student's learning in the recommended areas"
        ],
        "Practical_Tips": [
            "Best practices, tips, and advice for effectively learning and applying new concepts"
        ],
        "Real_World_Applications": ["Suggestions on how to apply the new skills and knowledge in practical, real-world scenarios"]
    }}

    Review the tips to ensure they are tailored to the student's academic and professional development needs, and provide them with a clear path for growth.

    Resume Text: '''{resume_text}'''
    """
    temperature = random.random()
    print(f"Temperature: {temperature}")
    return get_completion(prompt, temp = temperature)

def LLM_recommend_tips_2(resume_text):
    prompt = f"""
    You are an expert career advisor specializing in technology and engineering fields.
    Given the resume text of a student, your task is to provide concise and actionable learning tips based on their Preference field, experience, skills, and summary provided in the resume.

    The tips should:
    - Directly address areas where the student can expand their knowledge and skills.
    - Offer clear, practical advice that the student can easily implement.
    - Include recommendations for key resources that will help the student grow in their domain.

    Provide your recommendations in the following JSON format:
    {{
        "Focus_Areas": "A brief list of key areas where the student should focus their learning efforts",
        "Specific_topic": "A new specific topic for his profile in the focus area he is interested in",
        "Actionable_Tips": [
            "A few direct, practical tips the student can follow to enhance their skills and knowledge"
        ],
        "Resource_Recommendations": [
            "Specific resources such as links, books, or courses that will aid the student's growth"
        ]
    }}

    Ensure that the tips are relevant to the student's current experience and help them build towards their future goals.

    Resume Text: '''{resume_text}'''
    """
    temperature = random.random()
    print(f"Temperature: {temperature}")
    return get_completion(prompt, temp = temperature)

def LLM_structure_project(project_text):
    prompt = f"""
    You are an expert in project design, specializing in technology and engineering fields.
    Given the text of a project, your task is to structure it into a clear, concise, and actionable format. The structured output should include key details such as the project's title, a comprehensive description, relevant categories, required skills, and proposed algorithms.

    The project should be:
    - Clearly defined with a unique and informative title.
    - Described in detail, outlining the project's objectives, scope, and relevance.
    - Categorized appropriately based on its core domain (e.g., web, AI, etc.).
    - Matched with the necessary skills required to successfully complete the project.
    - Accompanied by proposed algorithms or methodologies that could be employed.

    Provide your structured output in the following JSON format:
    {{
        "ID": "A unique identifier for the project",
        "title": "A concise, descriptive title for the project",
        "description": "A detailed description of the project, including its objectives and relevance",
        "category": "Web",
        "required_skills": ["List of skills needed to complete the project"],
        "proposed_algorithms": ["List of algorithms or methodologies proposed for the project"]
    }}

    Review the project to ensure it is well-defined, feasible, and aligned with the intended learning outcomes.

    Project Text: '''{project_text}'''
    """
    return get_completion(prompt)

def LLM_prompt_RAG(resume_text, preference, context):
    prompt = f"""
    You are an expert career advisor specializing in technology and engineering fields. 
    Given the resume text of a student, and his preferences.
    Your task is to recommend based ONLY on the given context below, a suitable project for experience, skills, and summary provided in the resume.
    The recommended project should be:
    - Develop a project that is unique and innovative, clearly different from any of the student's previous work.
    - Designed to enhance and expand the student's knowledge and abilities, pushing their boundaries to explore new areas.
    - Resourceful: suggest links, techniques, text book references and examples in the steps and tips.

    Provide your recommendation in the following JSON format:
    {{
        "Project_Name": "A concise, descriptive name for the project",
        "Project_Description": "A detailed description of the project, including its objectives and relevance to the student's background",
        "Project_Steps": [
            "A list of clear, actionable steps to build the project (version 0)"
        ],
        "Project_Requirements": [
            "A list of required knowledge, tools, and resources needed for the project"
        ],
        "Project_Tips": [
            "Helpful tips and best practices for successfully completing the project"
        ],
        "Project_Applications": ["Applications to apply this project in real life"]
    }}

    Review the project to ensure it is feasible and beneficial for the student's academic and professional development, and ensure that it is not a mere repetition of their previous work.

    Resume Text: '''{resume_text}'''
    Preferences: '''{preference}'''
    Here are all the projects you have to recommend from: '''{context}'''
    """
    return get_completion(prompt)