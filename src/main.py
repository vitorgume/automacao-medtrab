# main.py
from fastapi import FastAPI
from src.controller.automacao_controller import router as automacao_router

app = FastAPI(title="Minha API FastAPI")

app.include_router(automacao_router)

@app.get("/health")
def health():
    return {"status": "ok"}
