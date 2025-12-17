import pandas as pd


def chapter_difficulty(df):
    chapter_stats = []

    grouped = df.groupby("chapter_order")

    for chapter, group in grouped:
        avg_time = group["time_spent"].mean()
        avg_score = group["score"].mean()

        # Dropout: students whose completion_status = 0 at this chapter
        dropout_rate = (group["completion_status"] == 0).mean()

        chapter_stats.append({
            "chapter": int(chapter),
            "avg_time": avg_time,
            "avg_score": avg_score,
            "dropout_rate": dropout_rate
        })

    stats_df = pd.DataFrame(chapter_stats)

    # Normalize
    stats_df["time_norm"] = stats_df["avg_time"] / stats_df["avg_time"].max()
    stats_df["dropout_norm"] = stats_df["dropout_rate"] / max(
        stats_df["dropout_rate"].max(), 0.01
    )
    stats_df["score_norm"] = stats_df["avg_score"] / 100

    stats_df["difficulty_score"] = (
        0.4 * stats_df["time_norm"] +
        0.4 * stats_df["dropout_norm"] +
        0.2 * (1 - stats_df["score_norm"])
    )

    return stats_df[[
        "chapter",
        "difficulty_score",
        "avg_time",
        "avg_score",
        "dropout_rate"
    ]].sort_values("difficulty_score", ascending=False).to_dict(orient="records")
