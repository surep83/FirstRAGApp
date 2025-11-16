from fastapi import APIRouter
from pydantic import BaseModel
from llm_chain.rag_chain import rag_pipeline
from llm_chain.response_formatter import format_response

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
    status: str = "success"
    type: str = "rag_response"

@router.post("/chat")
def chat_endpoint(request: QueryRequest) -> QueryResponse:
    """
    Receives a user query, passes it to the RAG pipeline,
    and returns the formatted answer.
    """
    try:
        answer = rag_pipeline(request.query)
        formatted = format_response(answer)
        return QueryResponse(**formatted)
    except Exception as e:
        return QueryResponse(answer=f"Error processing query: {str(e)}", status="error")