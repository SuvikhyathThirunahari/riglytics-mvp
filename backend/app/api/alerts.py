from fastapi import APIRouter

from app.services.alert_service import generate_alerts
from app.config import SAMPLE_DATA_PATH

router = APIRouter()


@router.get(
    "/alerts",
    tags=["Analytics"],
    summary="Generate drilling alerts",
    description="Returns operational alerts such as pressure spikes, RPM drops, and temperature spikes."
)
def get_alerts():
    """
    Return drilling alerts.
    """

    return generate_alerts(SAMPLE_DATA_PATH)