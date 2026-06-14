import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "..",
    "data"
)

UPLOAD_DIR = os.path.join(
    DATA_DIR,
    "uploads"
)

SAMPLE_DATA_PATH = os.path.join(
    DATA_DIR,
    "sample",
    "drilling_data.csv"
)

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)