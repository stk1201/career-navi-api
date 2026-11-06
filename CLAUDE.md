# キャリア逆算ナビ API

## 概要
就活生向けのキャリア診断Webアプリのバックエンド。
価値観の質問への回答から、職種データ（スペシャリスト／テックリード／PM／EM／CTO／起業）との
マッチ度をGeminiで診断し、結果カードとオリジナルキャラクター画像を生成する。
目的はポートフォリオ兼、クラウド（Google Cloud）の実務経験を積むこと。

## 技術スタック
- バックエンド：Python 3.12 / FastAPI / Cloud Run
- 生成AI（文章）：Gemini API（Google AI Studio の無料枠、google-genai SDK、構造化出力）
- 生成AI（画像）：Gemini（Vertex AI、google-genai SDK）※ステップ4
- DB：Firestore（ステップ3）／ストレージ：Cloud Storage（ステップ4）
- 運用：Secret Manager / IAM / GitHub Actions（ステップ5）/ Terraform（ステップ6、任意）
- フロントエンド：Next.js + TypeScript（別リポジトリ career-navi-web で作る）

## 決まっている設定
- リポジトリ：このフォルダ（career-navi-api）がGitリポジトリのルート
- Python仮想環境の名前：career（career/ はGitとDockerに含めない）
- GCPプロジェクトID：career-navi-fs
- リージョン：asia-northeast1
- Cloud Runサービス名：career-navi-api（--max-instances 1）
- Cloud Run用サービスアカウント：career-navi-run（最小権限）
- APIキーはSecret Managerで管理し、コードやファイルに絶対に書かない

## ロードマップ
1. 最小のFastAPI（/health）をCloud Runに公開
2. Secret Manager + Geminiで診断API（/careers, /diagnose）
3. Firestoreに職種データと診断結果を保存、共有URL発行、CORS設定
4. Gemini画像生成 + Cloud Storage、OGP
5. GitHub Actionsで自動デプロイ
6. Terraformでインフラをコード化（任意）

## 進め方のルール
- 私はクラウド初心者で、Dockerは少し経験がある程度。説明は日本語で、初心者向けにする
- コマンドを実行する前に、何をするコマンドか・各オプションの意味を説明する
- gcloudでリソースを作成・変更するコマンドや、料金が発生しうる操作は、実行前に必ず確認を取る
- 1ステップずつ進め、ステップの最後に動作確認の方法を示す
- コミットはステップの区切りごとに、内容がわかるメッセージで行う
- commitの前に、仮想環境や秘密情報が含まれていないか git status で確認する
