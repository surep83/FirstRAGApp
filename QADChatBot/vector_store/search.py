def search_kb(vector_store, query: str, top_k: int = 3):
    """
    Perform similarity search in the vector store.
    Args:
        vector_store: Chroma or Pinecone instance.
        query: User query string.
        top_k: Number of results to retrieve.
    Returns:
        List of Document objects.
    """
    retriever = vector_store.as_retriever(search_kwargs={"k": top_k})
    return retriever.get_relevant_documents(query)