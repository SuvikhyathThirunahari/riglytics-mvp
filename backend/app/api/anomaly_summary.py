from fastapi import APIRouter

from app.services.anomaly_service import detect_anomalies
from app.config import LATEST_UPLOAD_PATH

router = APIRouter()


@router.get(
    "/anomaly-summary",
    tags=["Analytics"]
)
def anomaly_summary():

    anomalies = detect_anomalies(
        LATEST_UPLOAD_PATH
    )

    return {
        "count": len(anomalies)
    }