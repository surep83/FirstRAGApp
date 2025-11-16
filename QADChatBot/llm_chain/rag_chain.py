import os
import sys
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, HuggingFaceEmbeddings
# from llm_chain.prompt_templates import build_prompt
"""
# Ensure project root is on sys.path so imports like `llm_chain.prompt_templates` resolve
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Add project root to sys.path
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from vector_store.connector import connect_vector_db

load_dotenv()

def rag_pipeline(query: str) -> str:

    # RAG pipeline: retrieve context from vector DB, build prompt, call LLM.
    # Uses free HuggingFace embeddings and HuggingFace LLM (completely free).

    try:
        # Connect to vector store with HuggingFace embeddings (free)
        vector_store = connect_vector_db(
            embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        )
        retriever = vector_store.as_retriever(search_kwargs={"k": 3})
        print("✅ Connected to vector store")
        # Retrieve relevant documents
        context_docs = retriever.invoke(query)

        # Build prompt from context
       # context_text = "\n".join([doc.page_content for doc in context_docs])
       # prompt = f"Based on the following context, answer the question:\n\nContext:\n{context_text}\n\nQuestion: {query}\n\nAnswer:"
        # prompt = build_prompt(query, context_docs)
        print("✅ Built RAG prompt")
        # Call HuggingFace LLM (free, no API quota issues)
        llm = HuggingFaceEndpoint(
            repo_id="mistralai/Mistral-7B-Instruct-v0.1",
            temperature=0.7,
            max_new_tokens=512
        )
        
        prompt = "Write a short poem about AI and nature."
        print(f"✅ Calling HuggingFace LLM... {prompt}")
        response = llm.invoke(prompt)
        print("✅ Received response from LLM")
        return response.strip()
    except Exception as e:
        return f"Error in RAG pipeline: {str(e)}"
    
rag_pipeline("Explain the theory of relativity in simple terms.")

"""

import os
from langchain_core.prompts import PromptTemplate


llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",
    max_new_tokens=512,
    top_k=10,
    top_p=0.95,
    typical_p=0.95,
    temperature=0.01,
    repetition_penalty=1.03,

)
print(llm.invoke("What is Deep Learning?"))