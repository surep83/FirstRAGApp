from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.constants import CHUNK_SIZE, CHUNK_OVERLAP

def split_text(docs):
    """
    Split documents into smaller chunks for embedding using config constants.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    return splitter.split_documents(docs)