# RAG Pipeline using LangChain and FAISS

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline using LangChain, FAISS, and Large Language Models (LLMs). The system retrieves relevant information from a knowledge base and generates context-aware responses to user queries.

## Features

* Retrieval-Augmented Generation (RAG)
* Document indexing using FAISS
* Semantic search with embeddings
* Context-aware question answering
* Flask-based web interface
* Environment variable management using `.env`

## Tech Stack

* Python
* LangChain
* FAISS
* Flask
* Hugging Face Embeddings
* Groq LLM API
* HTML, CSS, JavaScript

## Project Structure

```text
RAG_PIPELINE_LANGCHAIN/
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
├── .env
├── faiss_index/
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/Fathima-Sherin112/GenAI.git
cd GenAI/RAG_PIPELINE_LANGCHAIN
```

### Create Virtual Environment

```bash
python -m venv rag_env
```

### Activate Virtual Environment

Windows:

```bash
rag_env\Scripts\activate
```

Linux/Mac:

```bash
source rag_env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

## Run the Application

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

## How It Works

1. Documents are converted into embeddings.
2. Embeddings are stored in a FAISS vector database.
3. User queries are embedded and matched against stored vectors.
4. Relevant context is retrieved.
5. The LLM generates an answer using the retrieved context.

## Future Improvements

* PDF document ingestion
* Multi-document support
* Conversational memory
* Docker deployment
* Cloud deployment using AWS

## Author

**Fathima Sherin**

* GitHub: https://github.com/Fathima-Sherin112
* LinkedIn: https://linkedin.com/in/fathimasherin01
