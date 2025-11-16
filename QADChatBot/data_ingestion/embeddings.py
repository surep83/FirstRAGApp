from langchain_openai import OpenAIEmbeddings

def get_embeddings():
    """
    Initialize OpenAI embeddings model.
    """
    return OpenAIEmbeddings()