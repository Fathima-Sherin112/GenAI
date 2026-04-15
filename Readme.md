# AI Resume Analyzer 🚀

## 📌 Project Overview

The **AI Resume Analyzer** is a web-based application that analyzes resumes using **Google Gemini AI**. It extracts content from PDF resumes (including scanned/image-based PDFs using OCR) and provides detailed insights such as:

* Skills evaluation
* Strengths and weaknesses
* Suggested improvements
* Recommended courses
* Job role alignment
* Comparison with job descriptions

---

## 🧠 Features

✅ Upload PDF resumes
✅ Extract text from:

* Normal PDFs (using pdfplumber)
* Scanned PDFs (using OCR via pytesseract)

✅ AI-powered analysis using Gemini
✅ Job description comparison
✅ Clean UI with Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Google Gemini API**
* **pdfplumber**
* **pytesseract (OCR)**
* **pdf2image**
* **Pillow**

---

## 📂 Project Structure

```
resume-analyser/
│── app.py
│── requirements.txt
│── README.md
│── .env
```

---

## ⚙️ Installation

### 1. Clone Repository

```
git clone https://github.com/your-username/GENAi.git
cd GENAi/resume-analyser
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file in the project folder:

```
api_key=your_gemini_api_key_here
```

⚠️ Do NOT share your API key publicly.

---

## ▶️ Run the Application

```
streamlit run app.py
```

---

## 📥 How It Works

1. Upload your resume (PDF format)
2. (Optional) Enter job description
3. Click **Analyze Resume**
4. Get AI-generated insights

---

## 📊 Output Includes

* Profile evaluation
* Skills identified
* Missing skills
* Suggested improvements
* Recommended courses
* Job fit analysis

---

## 🚀 Future Improvements

* ATS score generation
* Resume scoring dashboard
* Downloadable report (PDF)
* Multi-role job matching
* Deploy using Streamlit Cloud

---

## 👩‍💻 Author

**Fathima Sherin**


