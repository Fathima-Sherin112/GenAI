import os

from dotenv import load_dotenv

load_dotenv()
import re

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

PDF_PATH = r"C:\Users\user\Downloads\DL_Adv\RAG_PIPELINE_LANGCHAIN\REST API Crash Course - Concepts, Python, Flask, Postgres.pdf"

print("Loading PDF...")

loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

print(f"Loaded {len(documents)} pages")


def clean(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"Page\s+\d+", "", text)
    text = re.sub(r"[^\w\s\.,!?]", "", text)
    return text.strip()


for doc in documents:
    doc.page_content = clean(doc.page_content)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", ".", " "]
)

chunks = splitter.split_documents(documents)

print(f"{len(chunks)} chunks created")

for i, chunk in enumerate(chunks):
    chunk.metadata.update(
        {
            "chunk_id": i,
            "category": "rest_api",
            "year": 2025
        }
    )

print("Loading Embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    model_kwargs={"device": "cpu"}
)

print("Creating FAISS Index...")

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

vector_store.save_local("faiss_index")

print("FAISS Index Saved Successfully")

# -------------------------
# Query Validation
# -------------------------

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()


def mask_pii(text):
    results = analyzer.analyze(
        text=text,
        language="en"
    )

    return anonymizer.anonymize(
        text=text,
        analyzer_results=results
    ).text


def validate_query(query):

    banned = [
        "ignore previous",
        "jailbreak",
        "disregard"
    ]

    for word in banned:
        if word in query.lower():
            raise ValueError("Invalid query detected")

    return mask_pii(query.strip())


# -------------------------
# Embeddings
# -------------------------

print("Loading Embeddings...")

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    model_kwargs={"device": "cpu"}
)

# -------------------------
# Load FAISS
# -------------------------

print("Loading FAISS Index...")

from langchain_community.vectorstores import FAISS

vector_store = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# -------------------------
# Retriever
# -------------------------

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)

# -------------------------
# LLM
# -------------------------

print("Loading LLM...")

from langchain_groq import ChatGroq

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# -------------------------
# Prompt
# -------------------------

from langchain_core.prompts import PromptTemplate

qa_prompt = PromptTemplate(
    template="""
You are a helpful AI assistant.

Answer ONLY from the provided context.

If the answer cannot be found in the context,
reply exactly:

I could not find this information in the document.

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)

# -------------------------
# RAG Chain
# -------------------------

from langchain.chains import RetrievalQA

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={
        "prompt": qa_prompt
    }
)

print("RAG Pipeline Ready")


# -------------------------
# Main Function
# -------------------------

def get_answer(user_query):

    try:

        safe_query = validate_query(
            user_query
        )

        result = rag_chain.invoke(
            {"query": safe_query}
        )

        return result["result"]

    except Exception as e:

        return f"Error: {str(e)}"