import argparse
import json
from src.ingestion import load_csv
from src.preprocessing import validate_data
from src.features import build_features
from src.model import load_model, predict_completion
from src.risk import assign_risk
from src.chapters import chapter_difficulty
from src.insights import generate_insights


def main():
    parser = argparse.ArgumentParser(
        description="AI Kata – Learning Intelligence CLI Tool"
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to input CSV file"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output.json",
        help="Path to output report JSON"
    )

    args = parser.parse_args()

    # 1. Load data
    data = load_csv(args.input)

    # 2. Validate & preprocess
    clean_data = validate_data(data)

    # 3. Feature engineering
    features = build_features(clean_data)

    # 4. Load trained model
    model = load_model("models/completion_model.pkl")

    # 5. Predict completion
    predictions = predict_completion(model, features)

    # 6. Risk detection
    risk_flags = assign_risk(predictions, features)

    # 7. Chapter difficulty analysis
    chapter_scores = chapter_difficulty(clean_data)

    # 8. Generate insights
    insights = generate_insights(
        predictions, risk_flags, chapter_scores
    )

    # 9. Final output
    output = {
        "predictions": predictions,
        "risk_flags": risk_flags,
        "chapter_difficulty": chapter_scores,
        "insights": insights
    }

    with open(args.output, "w") as f:
        json.dump(output, f, indent=4)

    print(f"✅ AI analysis complete. Output saved to {args.output}")


if __name__ == "__main__":
    main()
