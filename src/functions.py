import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
# import fitz
from docx import Document
import requests
from io import StringIO

# for testing locally --------------------------------------
load_dotenv()
goog_api_key = os.getenv('GOOGLE_API_KEY') # create a variable in .env file 'GOOGLE_API_KEY' and add the api key there

# # for testing on streamlit share -----------------------------
# goog_api_key = st.secrets['GOOGLE_API_KEY']

def compare_resume(resume_text, jd_text):
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(f"""
    Resume: ```{resume_text}```
    Job Description: ```{jd_text}```
    Given the above resume and job description delineated by ```, identify the skills and qualifications from both.
    Compare them to determine any skill gaps and estimate how qualified the individual is for the job.
    Give a percentage estimating how qualified the individual is for the job.
    For candidate information section, please cite any applicable certifications they have.
    Please penalize heavily for any missing mandatory qualifications and reflect it in the percentage.

    Output format should be as below, with each section title in large font:

    Estimated qualification percentage:

    Candidate information
    Current location:
    College degree (Bachelor's or above):
    Japanese language ability:
    English language ability:

    Summary:
    (please give a short summary of candidate persona.
    example: junior level candidate with 2 years of experience in software engineering, proficient in Python, Java, and C++)

    Top 5 Skills and qualifications from resume:
    - skill1
    - skill2
    - skill3
    ...
    5 main skills and qualifications from job description:
    - skill1
    - skill2
    - skill3
    ...
    Skill gaps:
    - skill1
    - skill2
    - skill3
    ...
    """)

    answer = response.text

    return answer


# def read_pdf(resume_file):
#     doc = fitz.open(resume_file)
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     return text


############ try these??? since it was a file extraction issue

# def read_pdf(file):
#     try:
#         doc = fitz.open(stream=file.read(), filetype="pdf")
#         text = ""
#         for page in doc:
#             text += page.get_text()
#         return text
#     except Exception as e:
#         st.error(f"Error reading PDF file: {e}")
#         return ""





def read_doc(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text
