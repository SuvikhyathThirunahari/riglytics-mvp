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

LATEST_UPLOAD_PATH = os.path.join(
    UPLOAD_DIR,
    "latest_upload.csv"
)

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)