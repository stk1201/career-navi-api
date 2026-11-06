from pydantic import BaseModel

class Career(BaseModel):
    id: str
    name: str
    summary: str
    values: list[str]

CAREERS: list[Career] = [
    Career(
        id="specialist",
        name="スペシャリスト",
        summary="特定の技術領域を深く極め、専門性で価値を出す。",
        values=["専門性", "探究心", "技術へのこだわり", "個人の成果"],
    ),
    Career(
        id="tech_lead",
        name="テックリード",
        summary="チームの技術的な方針を決め、設計とコードの品質を引っ張る。",
        values=["技術的リーダーシップ", "設計", "チームの生産性", "現場で手を動かす"],
    ),
    Career(
        id="pm",
        name="プロダクトマネージャー（PM）",
        summary="ユーザーと事業の課題から、何を作るべきかを決める。",
        values=["ユーザー視点", "意思決定", "ビジネス", "調整力"],
    ),
    Career(
        id="em",
        name="エンジニアリングマネージャー（EM）",
        summary="エンジニアの成長と組織づくりで、チームの成果を最大化する。",
        values=["人の成長", "組織づくり", "対話", "チームの成果"],
    ),
    Career(
        id="cto",
        name="CTO",
        summary="経営の視点で技術戦略を描き、技術組織全体に責任を持つ。",
        values=["経営視点", "技術戦略", "大きな責任", "組織全体への影響"],
    ),
    Career(
        id="founder",
        name="起業",
        summary="自ら事業を立ち上げ、ゼロから価値を生み出す。",
        values=["挑戦", "裁量", "リスクを取る", "社会へのインパクト"],
    ),
]
