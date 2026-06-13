from fastapi import APIRouter, UploadFile, File
import os

from app.services.csv_service import process_csv

router = APIRouter()


@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):

    upload_dir = "../data/uploads"

    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    result = process_csv(file_path)

    return {
        "filename": file.filename,
        **result
    }