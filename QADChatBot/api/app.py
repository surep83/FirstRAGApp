import os
import sys
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

# Add project root to sys.path for imports
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from api.routes import router

# Create FastAPI app instance
app = FastAPI(title="QAD Chatbot API", version="1.0.0")

# Include routes
app.include_router(router)

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)