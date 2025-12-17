import pandas as pd
from src.features import build_features


def test_feature_generation():
    data = pd.DataFrame({
        "student_id": ["S1", "S1"],
        "chapter_order": [1, 2],
        "time_spent": [30, 40],
        "score": [80, 70],
        "completion_status": [1, 0]
    })

    features = build_features(data)

    assert features.iloc[0]["avg_score"] == 75
    assert features.iloc[0]["score_trend"] == -10
