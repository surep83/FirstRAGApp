import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API keys and configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VECTOR_DB_URL = os.getenv("VECTOR_DB_URL")  # Optional for Pinecone or other DBs
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", "vector_store")  # Default local path