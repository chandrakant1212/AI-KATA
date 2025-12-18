from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import tempfile, os

from src.preprocessing import validate_data
from src.features import build_features
from src.model import load_model, predict_completion
from src.risk import assign_risk
from src.chapters import chapter_difficulty
from src.insights import generate_insights

app = FastAPI(title="AI Kata – Learning Intelligence")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

model = load_model("models/completion_model.pkl")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze-ui")
async def analyze_ui(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(await file.read())
        path = tmp.name

    df = pd.read_csv(path)
    os.remove(path)

    df = validate_data(df)
    features = build_features(df)
    predictions = predict_completion(model, features)
    risks = assign_risk(predictions, features)
    chapters = chapter_difficulty(df)
    insights = generate_insights(predictions, risks, chapters)

    return {
        "predictions": predictions,
        "risk_flags": risks,
        "chapter_difficulty": chapters,
        "insights": insights
    }

@app.get("/")
def root():
    return {
        "message": "AI Kata – Learning Intelligence API is running. Visit /docs for usage."
    }
