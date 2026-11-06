"""
仮想環境
source career/bin/activate

動作確認
uvicorn main:app --reload --port 8000
"""
import logging
from fastapi import FastAPI, HTTPException

from careers import CAREERS, Career
from questions import QUESTIONS, QUESTIONS_BY_ID, Question
from diagnosis import DiagnoseRequest, DiagnoseResult, diagnose

logger = logging.getLogger("uvicorn.error")
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/careers", response_model=list[Career])
def list_career():
    return CAREERS

@app.get("/careers/{career_id}", response_model=Career)
def get_career(career_id: str):
    for career in CAREERS:
        if career.id == career_id:
            return career
    raise HTTPException(status_code=404, detail="Career not found")

@app.get("/questions", response_model=list[Question])
def list_questions():
    return QUESTIONS

@app.post("/diagnose", response_model = DiagnoseResult)
def diagnose_endpoint(req: DiagnoseRequest):
    for a in req.answers:
        if a.question_id not in QUESTIONS_BY_ID:
            raise HTTPException(status_code=422, detail=f"不明な質問IDです: {a.question_id}")

    try:
        return diagnose(req)
    except Exception:
        logger.exception("diagnose failed")
        raise HTTPException(status_code=502, detail="診断に失敗しました。時間をおいて再度お試しください。")
