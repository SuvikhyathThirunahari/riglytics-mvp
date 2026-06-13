from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.summary import router as summary_router
from app.api.charts import router as charts_router
from app.api.anomalies import router as anomalies_router
from app.api.alerts import router as alerts_router

app = FastAPI(
    title="RigLytics API",
    version="1.0.0"
)

app.include_router(upload_router)
app.include_router(summary_router)
app.include_router(charts_router)
app.include_router(anomalies_router)
app.include_router(alerts_router)


@app.get("/")
def root():
    return {
        "message": "RigLytics Backend Running"
    }