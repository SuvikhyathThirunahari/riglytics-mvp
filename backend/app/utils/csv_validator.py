import os

import pandas as pd


REQUIRED_COLUMNS = [
    "timestamp",
    "depth",
    "pressure",
    "rpm",
    "temperature",
    "wob"
]


def validate_csv(file_path):
    """
    Validate drilling CSV file.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError(
            "CSV file is empty."
        )

    missing_columns = [
        col
        for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    return df