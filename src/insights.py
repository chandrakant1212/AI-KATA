def generate_insights(predictions, risk_flags, chapter_scores):
    insights = []

    # Student risk insights
    for r in risk_flags:
        if r["risk_level"] == "HIGH":
            insights.append(
                f"Student {r['student_id']} is at HIGH risk of dropping out and requires early intervention."
            )

    # Chapter difficulty insights
    if chapter_scores:
        hardest = chapter_scores[0]
        insights.append(
            f"Chapter {hardest['chapter']} is the most difficult chapter with "
            f"a dropout rate of {hardest['dropout_rate']:.0%} and "
            f"average score of {hardest['avg_score']:.1f}."
        )

    # Model-level insight
    avg_prob = sum(p["completion_probability"] for p in predictions) / len(predictions)
    insights.append(
        f"Overall course completion probability across students is {avg_prob:.2f}."
    )

    return insights
