import os

from google import genai
from google.genai import types
from pydantic import BaseModel, Field

from careers import CAREERS
from questions import QUESTIONS_BY_ID

MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash-lite")

# ---- リクエスト（フロントエンドから受け取るデータ） ----
class Answer(BaseModel):
    question_id:str
    answer: str = Field(max_length=500)

class DiagnoseRequest(BaseModel):
    answers: list[Answer] = Field(min_length=1, max_length=10)

# ---- レスポンス（Gemini に作らせ、フロントエンドに返すデータ） ----
class CareerMatch(BaseModel):
    career_id: str
    score: int
    reason: str

class DiagnoseResult(BaseModel):
    top_career_id: str
    summary: str
    matches: list[CareerMatch]

def build_prompt(req: DiagnoseRequest) -> str:
    """
    Gemini に投げるプロンプトを作る
    """
    careers_text = "\n".join(
        f"- id: {c.id} / {c.name} : {c.summary} (大事にする価値観：{','.join(c.values)}) "
        for c in CAREERS
    )

    answers_text = "\n".join(
        f"Q: {QUESTIONS_BY_ID[a.question_id].text}\nA: {a.answer}" for a in req.answers
    )

    return f"""あなたは就活生向けのキャリアアドバイザーです。
以下の職種一覧と、就活生の価値観に関する回答を読み、各職種とのマッチ度を診断してください。

# 職種一覧
{careers_text}

# 就活生の回答
{answers_text}

# 出力ルール
- matches には6職種すべてを含め、score は0〜100の整数にする
- career_id には職種一覧の id をそのまま使う
- top_career_id は最も score が高い職種の id にする
- reason は回答の内容に触れながら、2文程度で書く
- summary は就活生への励ましを含めて、3文程度で書く
"""

def diagnose(req: DiagnoseRequest) -> DiagnoseResult:
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"]) # Geminiと通信するための窓口を作成
    # Geminiにプロンプトを送り、レスポンスを受け取る
    response = client.models.generate_content(
        model=MODEL,
        contents=build_prompt(req),
        config=types.GenerateContentConfig(
            response_mime_type="application/json", # json形式で返してもらう
            response_schema=DiagnoseResult, # レスポンスの型を指定
        ),
    )
    return DiagnoseResult.model_validate_json(response.text) #レスポンスがJSON文字列なおかをPydanticで検証し、DiagnoseResult型に変換して返す
