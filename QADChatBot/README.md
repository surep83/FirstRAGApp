# RAG Application Template

## Overview
This template includes:
- FastAPI backend for chatbot
- LangChain-style RAG pipeline
- Streamlit UI for user interaction

## Project Structure
rag_app/
  ├── config/ (settings.py, constants.py)
  ├── data_ingestion/ (loaders.py, chunking.py, embeddings.py)
  ├── vector_store/ (connector.py, search.py)
  ├── llm_chain/ (rag_chain.py, prompt_templates.py, response_formatter.py)
  ├── api/ (routes.py, controllers.py)
  ├── ui/ (chatbot_app.py)
  ├── utils/ (logger.py, file_utils.py)
  ├── tests/ (test_app.py)
  └── main.py

## Setup Instructions
1. Create virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Configure `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
VECTOR_DB_URL=your_vector_db_url_here
EMBEDDING_MODEL=text-embedding-ada-002
```

3. Start FastAPI backend:
```
# Activate virtual env
.venv\Scripts\Activate.ps1

# Run uvicorn on port 8501
python -m uvicorn api.app:app --host 127.0.0.1 --port 8501 --reload
```

4. Launch Streamlit UI:
```
streamlit run ui/chatbot_app.py
```
