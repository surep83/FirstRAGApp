import os
from typing import Optional
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

def connect_vector_db(embeddings=None, persist_dir: str = "vector_store", pinecone_index: Optional[str] = None):
    """
    Connect to a vector DB and return a LangChain-compatible vectorstore instance.
    Supports:
      - Pinecone (if PINECONE_API_KEY and PINECONE_ENV/PINECONE_REGION are set or VECTORDB=pinecone)
      - Chroma (local, default)

    Args:
      embeddings: an embeddings object (required for Pinecone; optional for Chroma)
      persist_dir: directory for Chroma persistence
      pinecone_index: explicit Pinecone index name (falls back to PINECONE_INDEX env var)

    Returns:
      A vectorstore instance (Pinecone or Chroma)
    """
    # Prefer explicit env switch, otherwise auto-detect by presence of Pinecone keys
    # use_pinecone = os.getenv("VECTORDB", "").lower() == "pinecone" or bool(os.getenv("PINECONE_API_KEY"))

    # if use_pinecone:
    #     try:
    #         import pinecone
    #         from langchain.vectorstores import Pinecone as LC_Pinecone
    #     except Exception as e:
    #         raise RuntimeError("Pinecone libraries not available. Install pinecone-client and langchain.") from e

    #     if embeddings is None:
    #         raise ValueError("embeddings must be provided to connect to Pinecone")

    #     api_key = os.getenv("PINECONE_API_KEY")
    #     env = os.getenv("PINECONE_ENV") or os.getenv("PINECONE_REGION")
    #     if not api_key or not env:
    #         raise ValueError("PINECONE_API_KEY and PINECONE_ENV (or PINECONE_REGION) must be set for Pinecone")

    #     pinecone.init(api_key=api_key, environment=env)

    #     index_name = pinecone_index or os.getenv("PINECONE_INDEX")
    #     if not index_name:
    #         raise ValueError("Pinecone index name must be provided via pinecone_index or PINECONE_INDEX env var")

    #     # Connect to existing Pinecone index
    #     vectorstore = LC_Pinecone.from_existing_index(index_name, embedding=embeddings)
    #     print(f"Connected to Pinecone index: {index_name}")
    #     return vectorstore

    # Fallback to local Chroma
    try:
        from langchain_chroma import Chroma
    except Exception as e:
        raise RuntimeError("Chroma bindings not available. Install langchain-chroma or use Pinecone.") from e

    # If embeddings not provided, create a default HuggingFaceEmbeddings
    if embeddings is None:
        try:
            from langchain_huggingface import HuggingFaceEmbeddings
        except Exception as e:
            raise RuntimeError("HuggingFace embeddings package not available. Install langchain-huggingface.") from e
        model_name = os.getenv("HF_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
        embeddings = HuggingFaceEmbeddings(model_name=model_name)

    # Create or connect to Chroma vector store (persisted directory)
    try:
        vectorstore = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    except TypeError:
        # fallback if the Chroma wrapper uses different parameter names
        vectorstore = Chroma(persist_dir, embeddings)

    print(f"Using Chroma vector store at: {persist_dir}")
    return vectorstore
