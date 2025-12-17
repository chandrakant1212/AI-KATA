import pandas as pd
from src.risk import assign_risk


def test_risk_assignment():
    predictions = [
        {"student_id": "S1", "completion_probability": 0.3}
    ]

    features = pd.DataFrame([
        {"student_id": "S1", "avg_score": 45}
    ])

    risk = assign_risk(predictions, features)

    assert risk[0]["risk_level"] == "HIGH"
