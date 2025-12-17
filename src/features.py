import pandas as pd
import numpy as np


def build_features(df):
    """
    Converts chapter-level logs into student-level ML features
    """

    features = []

    grouped = df.groupby("student_id")

    for student_id, group in grouped:
        group = group.sort_values("chapter_order")

        avg_score = group["score"].mean()
        total_time = group["time_spent"].sum()
        chapters_completed = group["chapter_order"].nunique()
        time_per_chapter = total_time / chapters_completed

        # Score trend (last - first)
        score_trend = group["score"].iloc[-1] - group["score"].iloc[0]

        completion_status = group["completion_status"].iloc[-1]

        features.append({
            "student_id": student_id,
            "avg_score": avg_score,
            "total_time": total_time,
            "chapters_completed": chapters_completed,
            "time_per_chapter": time_per_chapter,
            "score_trend": score_trend,
            "completion_status": completion_status
        })

    return pd.DataFrame(features)
