from fastapi import APIRouter, UploadFile, File
import shutil

from app.services.csv_service import process_csv
from app.config import LATEST_UPLOAD_PATH

router = APIRouter()


@router.post(
    "/upload-csv",
    tags=["Upload"],
    summary="Upload drilling CSV",
    description="Uploads a drilling dataset and returns basic file statistics."
)
async def upload_csv(file: UploadFile = File(...)):

    with open(LATEST_UPLOAD_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_csv(LATEST_UPLOAD_PATH)

    return {
        "filename": file.filename,
        **result
    }