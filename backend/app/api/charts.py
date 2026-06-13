from fastapi import APIRouter

from app.services.chart_service import get_chart_data
from app.config import SAMPLE_DATA_PATH

router = APIRouter()


@router.get(
    "/chart-data",
    tags=["Analytics"],
    summary="Get chart-ready drilling data",
    description="Returns drilling records formatted for frontend chart visualization."
)
def chart_data():
    """
    Return drilling chart data.
    """

    return get_chart_data(SAMPLE_DATA_PATH)