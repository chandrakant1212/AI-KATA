import pandas as pd


def adapt_dataset(df):
    df = df.copy()
    metadata = {
        "chapter_signal": "observed",
        "completion_signal": "observed",
        "time_signal": "observed",
        "score_signal": "observed"
    }

    # ---------- Student ID ----------
    if "student_id" not in df.columns:
        df["student_id"] = df.index.astype(str)

    # ---------- Course ID ----------
    if "course_id" not in df.columns:
        df["course_id"] = "C01"

    # ---------- Chapter Order ----------
    if "chapter_order" not in df.columns:
        df["chapter_order"] = df.groupby("student_id").cumcount() + 1
        metadata["chapter_signal"] = "inferred"

    # ---------- Time Spent ----------
    if "time_spent" not in df.columns:
        for col in ["time", "duration", "studytime", "hours", "sum_click"]:
            if col in df.columns:
                df["time_spent"] = df[col]
                break
        else:
            raise ValueError("Time spent signal missing: required for chapter difficulty")

    # ---------- Score ----------
    if "score" not in df.columns:
        for col in ["score", "final_score", "grade", "G1", "G2", "G3"]:
            if col in df.columns:
                df["score"] = df[col]
                break
        else:
            raise ValueError("Score signal missing: required for prediction")

    # ---------- Completion Status ----------
    if "completion_status" not in df.columns:
        if "final_result" in df.columns:
            df["completion_status"] = df["final_result"].apply(
                lambda x: 1 if str(x).lower() in ["pass", "completed", "yes"] else 0
            )
        else:
            # Fallback inference (documented)
            df["completion_status"] = (df["score"] >= 50).astype(int)
            metadata["completion_signal"] = "inferred"

    required_cols = [
        "student_id",
        "course_id",
        "chapter_order",
        "time_spent",
        "score",
        "completion_status"
    ]

    return df[required_cols], metadata
