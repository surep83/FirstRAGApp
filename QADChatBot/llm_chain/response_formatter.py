import os
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from vector_store.connector import connect_vector_db
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint

# Add project root to sys.path
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

load_dotenv()

def format_response(response_text: str, include_metadata: bool = False) -> dict:
    """
    Format the LLM response into a structured response object.
    
    Args:
        response_text: The raw response from the LLM
        include_metadata: Whether to include additional metadata
    
    Returns:
        A dictionary with formatted response data
    """
    formatted = {
        "answer": response_text.strip() if response_text else "No answer generated",
        "status": "success",
        "type": "rag_response"
    }
    
    if include_metadata:
        from datetime import datetime
        formatted["metadata"] = {
            "model": "mistralai/Mistral-7B-Instruct-v0.1",
            "timestamp": str(datetime.now())
        }
    
    return formatted

