import pandas as pd


def load_csv(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        raise ValueError(f"Failed to load CSV: {e}")
