# main.py
from fastapi import FastAPI

app = FastAPI(title="Minha API FastAPI")

@app.get("/health")
def health():
    return {"status": "ok"}
