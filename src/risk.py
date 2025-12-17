def assign_risk(predictions, features_df):
    risk_results = []

    feature_map = {
        row["student_id"]: row
        for _, row in features_df.iterrows()
    }

    for pred in predictions:
        student_id = pred["student_id"]
        prob = pred["completion_probability"]

        avg_score = feature_map[student_id]["avg_score"]

        if prob < 0.4 or avg_score < 50:
            risk = "HIGH"
        elif prob < 0.7:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        risk_results.append({
            "student_id": student_id,
            "risk_level": risk
        })

    return risk_results
