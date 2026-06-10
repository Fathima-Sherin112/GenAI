import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
import pdfplumber
import pytesseract
from pdf2image import convert_from_path

#load enviornment variable
load_dotenv()

#config Google gemini_api
genai.configure(api_key=os.getenv("api_key"))

#function to extract text from pdf
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                text+=page_text
        if text.strip():
            return text.strip()

    except Exception as e:
        print(f"direct text extraction as failed : {e}")
    
    #if pdf is image based

    print("Falling back to OCR for image-based pdf")
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            image_text = pytesseract.image_to_string(image)
            text+=image_text + "\n"
    except Exception as e:
        print(f'OCR Failed : {e}')
    
    return text.strip()

#function to get response from Gemini AI
def analyse_resume(resume_text,job_description=None):
    if not resume_text:
        return("Resume text is required")
    model = genai.GenerativeModel("gemini-3-flash-preview")

    base_prompt = f'''You are an experienced HR with Technical Experience in the field of any one job role from Data Science, Data Analyst,
    DevOPS, Machine Learning Engineer, Prompt Engineer, AI Engineer, Full Stack Web Development, Big Data Engineering, Marketing Analyst,
    Human Resource Manager, Software Developer your task is to review the provided resume.
    Please share your professional evaluation on whether the candidate's profile aligns with the role. ALso mention Skills he already have
    and siggest some skills to imorve his resume, alos suggest some course he might take to improve the skills Highlight the strengths and 
    weaknesses.
    Resume :
    {resume_text}
    '''

    if job_description:
        base_prompt+= f'''
        Additionally,compare this resume to the folowing Job Description:

        Job Description:{job_description}

        Highlight the stregth and weaaknesses of the applicant in relation To the specified job requirements.
    
        '''

    respose = model.generate_content(base_prompt)
    analysis = respose.text.strip()
    return analysis

#streamlit APP
st.set_page_config(page_title="Resume Analyser",layout="wide")

st.title("AI Resume Analyser")
st.write("Analyse your resume Using Gemini")
col1,col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload your Resume as PDF",type=['pdf'])
with col2:
    jd = st.text_area("Enter the Job Description:",placeholder="Paste your description here")

if uploaded_file is not None:
    st.success("Resume uploaded Successfully")
else:
    st.warning("Error Found")

st.markdown("<div style= 'padding-top: 10px;'></div>",unsafe_allow_html=True)
if uploaded_file:
    with open("uploaded_resume.pdf","wb") as f:
        f.write(uploaded_file.getbuffer())
    resume_text = extract_text_from_pdf("uploaded_resume.pdf")

    if st.button("Analyze Resume"):
        with st.spinner("Analysing Resume...."):
            try:
                analysis = analyse_resume(resume_text,jd)
                st.success("Analysis completed")
                st.write(analysis)
            except Exception as e:
                st.error(f'Aaslysis failed : {e}')
                
