from pydantic import BaseModel

class Question(BaseModel):
    id: str
    text: str

QUESTIONS: list[Question] = [
    Question(id="q1", text="学生時代に一番夢中になったことは何ですか？その中でのあなたの役割も教えてください。"),
    Question(id="q2", text="仕事をしていて一番うれしいと感じるのは、どんな瞬間だと思いますか？"),
    Question(id="q3", text="難しい問題にぶつかったとき、あなたはまずどう動きますか？"),
    Question(id="q4", text="10年後、周りや社会にどんな影響を与えていたいですか？"),
]

QUESTIONS_BY_ID: dict[str, Question] = {q.id: q for q in QUESTIONS}
