import streamlit as st
from src.functions import compare_resume

def main():
    # Title
    st.title("ResumeFIt")
    st.write("Fill in the fields below to compare your resume to a job description.")

    # Input fields
    resume_text = st.text_input("Resume Information")
    jd_text = st.text_input("Job Description")

    # Submit button
    if st.button("Submit"):
        # Process the inputs
        process_inputs(compare_resume(resume_text, jd_text))

def process_inputs(input1):
    # Process the inputs here
    st.write("Your results: ", input1)


if __name__ == "__main__":
    main()
