import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from src.features import build_features
from src.ingestion import load_csv
from src.preprocessing import validate_data


def train():
    # Load and prepare data
    df = load_csv("data/sample_input.csv")
    df = validate_data(df)

    features_df = build_features(df)

    X = features_df.drop(columns=["student_id", "completion_status"])
    y = features_df["completion_status"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"Model Accuracy: {acc:.2f}")

    # Save model
    joblib.dump(model, "models/completion_model.pkl")
    print("✅ Model saved to models/completion_model.pkl")


if __name__ == "__main__":
    train()
