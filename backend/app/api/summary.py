from fastapi import APIRouter

from app.services.summary_service import get_summary_metrics
from app.config import LATEST_UPLOAD_PATH

router = APIRouter()


@router.get(
    "/summary",
    tags=["Analytics"],
    summary="Get drilling summary metrics",
    description="Returns aggregate drilling statistics including averages and maximum values."
)
def get_summary():
    """
    Return drilling summary metrics.
    """

    return get_summary_metrics(LATEST_UPLOAD_PATH)