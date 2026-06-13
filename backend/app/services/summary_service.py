from app.utils.csv_validator import validate_csv


def get_summary_metrics(file_path):
    """
    Calculate drilling summary metrics.
    """

    df = validate_csv(file_path)

    return {
        "total_records": len(df),
        "average_pressure": round(df["pressure"].mean(), 2),
        "average_rpm": round(df["rpm"].mean(), 2),
        "average_temperature": round(df["temperature"].mean(), 2),
        "average_wob": round(df["wob"].mean(), 2),
        "max_pressure": float(df["pressure"].max()),
        "max_temperature": float(df["temperature"].max())
    }