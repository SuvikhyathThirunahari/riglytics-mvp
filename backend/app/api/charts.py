from fastapi import APIRouter

from app.services.chart_service import get_chart_data
from app.config import LATEST_UPLOAD_PATH

router = APIRouter()


@router.get(
    "/chart-data",
    tags=["Analytics"],
    summary="Get chart-ready drilling data",
)
def chart_data():
    return get_chart_data(LATEST_UPLOAD_PATH)