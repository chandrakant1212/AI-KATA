import joblib


def load_model(path):
    try:
        return joblib.load(path)
    except Exception as e:
        raise ValueError(f"Could not load model: {e}")


def predict_completion(model, features_df):
    X = features_df.drop(columns=["student_id", "completion_status"])
    preds = model.predict(X)
    probs = model.predict_proba(X)[:, 1]

    results = []

    for i, student_id in enumerate(features_df["student_id"]):
        results.append({
            "student_id": student_id,
            "will_complete": int(preds[i]),
            "completion_probability": round(float(probs[i]), 3)
        })

    return results
