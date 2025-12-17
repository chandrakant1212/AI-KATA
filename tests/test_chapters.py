def test_chapter_difficulty_output():
    import pandas as pd
    from src.chapters import chapter_difficulty

    df = pd.DataFrame({
        "chapter_order": [1, 1, 2, 2],
        "time_spent": [30, 40, 60, 70],
        "score": [80, 75, 50, 45],
        "completion_status": [1, 1, 0, 0]
    })

    result = chapter_difficulty(df)
    assert len(result) == 2
