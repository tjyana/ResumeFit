import json
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
goog_api_key = os.getenv('GOOGLE_API_KEY') # create a variable in .env file 'GOOGLE_API_KEY' and add the api key there

def compare_resume(resume_text, jd_text):
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(f"""
    Resume: ```{resume_text}```
    Job Description: ```{jd_text}```
    Given the above resume and job description delineated by ```, identify the skills and qualifications from both.
    Then, compare them to determine any skill gaps and estimate how qualified the individual is for the job.
    Give a percentage estimating how qualified the individual is for the job.
    Output format should be as below:

    Skills and qualifications from resume:
    - skill1
    - skill2
    - skill3
    ...
    Skills and qualifications from job description:
    - skill1
    - skill2
    - skill3
    ...
    Skill gaps:
    - skill1
    - skill2
    - skill3
    ...

    Estimated qualification percentage: 80%

    """)

    answer = response.text


    return answer
