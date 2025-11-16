import os
import sys
from llm_chain.rag_chain import rag_pipeline

def handle_query(query: str) -> str:
    """Process user query and return response using RAG pipeline."""
    return rag_pipeline(query)
