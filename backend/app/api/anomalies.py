from fastapi import APIRouter

from app.services.anomaly_service import detect_anomalies
from app.config import SAMPLE_DATA_PATH

router = APIRouter()


@router.get(
    "/anomalies",
    tags=["Analytics"],
    summary="Detect drilling anomalies",
    description="Uses Isolation Forest to identify abnormal drilling conditions."
)
def get_anomalies():
    """
    Return drilling anomalies.
    """

    return detect_anomalies(SAMPLE_DATA_PATH)