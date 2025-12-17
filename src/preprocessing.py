REQUIRED_COLUMNS = [
    "student_id",
    "course_id",
    "chapter_order",
    "time_spent",
    "score",
    "completion_status"
]


def validate_data(df):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Drop rows with nulls in critical columns
    df = df.dropna(subset=REQUIRED_COLUMNS)

    # Type casting
    df["chapter_order"] = df["chapter_order"].astype(int)
    df["time_spent"] = df["time_spent"].astype(float)
    df["score"] = df["score"].astype(float)
    df["completion_status"] = df["completion_status"].astype(int)

    return df
