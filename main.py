import streamlit as st
from src.functions import read_resume
from io import StringIO
import PyPDF2


# # original code that works --------------------------------------

# def main():
#     # Title
#     st.title("ResumeFit")
#     st.write("Fill in the fields below to compare your resume to a job description.")

#     # Input fields
#     resume_text = st.text_input("Resume Information")
#     jd_text = st.text_input("Job Description")

#     # Submit button
#     if st.button("Submit"):
#         # Process the inputs
#         process_inputs(compare_resume(resume_text, jd_text))

# # original code that works --------------------------------------

def main():
    # Title
    st.sidebar.title("ResumeFit")
    st.sidebar.write("Fill in the fields below to compare your resume to a job description.")

    # Input fields

    # Resume Input
    st.sidebar.write("RESUME")

    # Select input method: Copy and paste text or upload a file
    resume_method = st.sidebar.selectbox("""Choose an input method:""", ("Text", "File"))


    # Input: Text
    if resume_method == "Text":
        resume_text = st.sidebar.text_area("Resume Text", height=200)

    # Input: File Upload
    elif resume_method == "File":

        # uploader
        resume_file = st.sidebar.file_uploader("Choose a PDF or DOC file", type=["pdf", "docx", "txt"])
        print('resume_file:', resume_file)

        # # read the file
        # if resume_file is not None:
        #     file_type = resume_file.name.split(".")[-1]
        #     print(file_type)

        #     # pdf file
        #     if file_type == "pdf":
        #         # read pdf
        #         resume_file.seek(0)
        #         reader = PyPDF2.PdfFileReader(resume_file)
        #         text = ''

        #         # extract text
        #         for i in range(reader.numPages):
        #             text += reader.getPage(i).extract_text()

        #         stringio = StringIO
        #         text = stringio.read()

        #         st.write(text)


        #     # docx file
        #     elif file_type == "docx":
        #         resume_text = read_doc(resume_file)
        #     else:
        #         st.write("Please upload a PDF or DOC file")
        #     # st.text_area("Extracted Text", resume_text, height=200)



    # # Job Description Input
    # st.sidebar.write("JOB DESCRIPTION")
    # jd_method = st.sidebar.selectbox("Choose an input method: ", ("Text", "File"))
    # if jd_method == "Text":
    #     jd_text = st.sidebar.text_area("Job Description Text", height=200)
    # elif jd_method == "File":
    #     jd_file = st.sidebar.file_uploader("Choose a PDF or DOC file ", type=["pdf", "docx"])
    #     if jd_file is not None:
    #         file_type = jd_file.name.split(".")[-1]
    #         if file_type == "pdf":
    #             jd_text = read_pdf(jd_file)
    #         elif file_type == "docx":
    #             jd_text = read_doc(jd_file)
    #         else:
    #             st.write("Please upload a PDF or DOC file")
    #         # st.text_area("Extracted Text", jd_text, height=200)






    # Submit button
    if st.sidebar.button("Submit"):
        # Process the inputs
        st.session_state.resume_file = resume_file
        # st.session_state.jd_text = jd_text
        st.header("Fit Score")
        # output = compare_resume(resume_text, jd_text)
        output = read_resume(resume_file)
        process_inputs(output)


def process_inputs(input1):
    # Function to display the final output
    # Process the inputs here
    st.write(" ", input1)


if __name__ == "__main__":
    main()
