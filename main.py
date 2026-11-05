"""
仮想環境
source career/bin/activate
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}
