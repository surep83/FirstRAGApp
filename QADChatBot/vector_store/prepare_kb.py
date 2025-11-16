"""
prepare_kb.py
This script loads documents from a specified folder, splits them into chunks,
generates embeddings using a free HuggingFace model, and stores them in a Chroma vector database.
Run this script before starting the Streamlit UI or FastAPI backend.
"""

import os
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader, UnstructuredExcelLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# ✅ Configuration
FOLDER_PATH = r"C:/Users/apas/OneDrive - Adient/Desktop/Train/"  # Change this to your SOP/documents folder
PERSIST_DIR = "vector_store"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

def load_documents(folder_path):
    supported_ext = {".pdf", ".docx", ".txt", ".xlsx"}
    documents = []
    for root, _, files in os.walk(folder_path):
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext not in supported_ext:
                continue
            full_path = os.path.join(root, fname)
            try:
                if ext == ".pdf":
                    loader = PyPDFLoader(full_path)
                elif ext == ".docx":
                    loader = Docx2txtLoader(full_path)
                elif ext == ".txt":
                    loader = TextLoader(full_path, encoding="utf-8")
                elif ext == ".xlsx":
                    loader = UnstructuredExcelLoader(full_path, mode="elements")
                else:
                    continue
                loaded_docs = loader.load()
                for d in loaded_docs:
                    if not hasattr(d, "metadata") or d.metadata is None:
                        d.metadata = {}
                    d.metadata.update({"source": full_path, "file_name": fname})
                documents.extend(loaded_docs)
            except Exception as e:
                print(f"Failed to load {full_path}: {e}")
    return documents

def split_text(docs, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)

def create_vector_store(chunks, persist_dir=PERSIST_DIR):
    # ✅ Use HuggingFace embeddings (free, local)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    print(f"✅ Vector store created and persisted at {persist_dir}")

if __name__ == "__main__":
    print("Loading documents...")
    docs = load_documents(FOLDER_PATH)
    print(f"Loaded {len(docs)} documents.")

    print("Splitting documents into chunks...")
    chunks = split_text(docs)
    print(f"Created {len(chunks)} chunks.")

    print("Creating vector store...")
    create_vector_store(chunks)
    print("✅ Knowledge base preparation complete!")
    print("You can now run the Streamlit UI or FastAPI backend to interact with the knowledge base.")
    print(docs)