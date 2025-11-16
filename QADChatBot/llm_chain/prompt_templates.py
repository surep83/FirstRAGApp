def build_prompt(query: str, context_docs: list) -> dict:
    """
    Construct a prompt and return it in dictionary form suitable for
    passing to HuggingFaceEndpoint.invoke().

    Returns:
      {
        "inputs": "<prompt string>",
        "parameters": {
          "max_new_tokens": int,
          "temperature": float,
          ...optional model params...
        },
        "meta": {
          "num_docs": int,
          "query": "<original query>"
        }
      }
    """
    # Build a readable context string from retrieved documents
    context_text = "\n\n".join(getattr(doc, "page_content", str(doc)) for doc in context_docs)

    prompt = (
        "You are a helpful assistant. Use the context below to answer the question.\n\n"
        f"Context:\n{context_text}\n\n"
        f"Question: {query}\n\n"
        "Answer:"
    )

    return {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "temperature": 0.7
        },
        "meta": {
            "num_docs": len(context_docs),
            "query": query
        }
    }