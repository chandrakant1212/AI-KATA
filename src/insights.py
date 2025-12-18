def generate_insights(predictions, risk_flags, chapter_scores, metadata=None):
    insights = []

    for r in risk_flags:
        if r["risk_level"] == "HIGH":
            insights.append(
                f"Student {r['student_id']} is at HIGH risk of dropping out."
            )

    hardest = chapter_scores[0]
    insights.append(
        f"Chapter {hardest['chapter']} requires improvement due to high dropout rate and low scores."
    )

    if metadata:
        inferred = [k for k, v in metadata.items() if v == "inferred"]
        if inferred:
            insights.append(
                f"Note: Some learning signals were inferred due to dataset limitations ({', '.join(inferred)})."
            )

    return insights
