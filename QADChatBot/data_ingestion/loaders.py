import os
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader, UnstructuredExcelLoader

def load_documents(folder_path: str):
    """
    Load documents from a folder (PDF, DOCX, TXT, XLSX).
    Returns a list of Document objects.
    """
    supported_ext = {".pdf", ".docx", ".txt", ".xlsx"}
    documents = []
    for root, _, files in os.walk(folder_path):
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext not in supported_ext:
                continue
            full_path = os.path.join(root, fname)
            try:
                if ext == ".pdf":
                    loader = PyPDFLoader(full_path)
                elif ext == ".docx":
                    loader = Docx2txtLoader(full_path)
                elif ext == ".txt":
                    loader = TextLoader(full_path, encoding="utf-8")
                elif ext == ".xlsx":
                    loader = UnstructuredExcelLoader(full_path, mode="elements")
                else:
                    continue
                docs = loader.load()
                for d in docs:
                    if not hasattr(d, "metadata") or d.metadata is None:
                        d.metadata = {}
                    d.metadata.update({"source": full_path, "file_name": fname})
                documents.extend(docs)
            except Exception as e:
                print(f"Failed to load {full_path}: {e}")
    return documents