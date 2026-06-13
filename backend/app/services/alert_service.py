from app.utils.csv_validator import validate_csv


def generate_alerts(file_path):
    """
    Generate drilling alerts based on threshold rules.
    """

    df = validate_csv(file_path)

    alerts = []

    for _, row in df.iterrows():

        if row["pressure"] > 4000:
            alerts.append({
                "timestamp": row["timestamp"],
                "alert_type": "Pressure Spike Detected",
                "severity": "High",
                "message": f"Pressure reached {row['pressure']} psi."
            })

        if row["rpm"] < 100:
            alerts.append({
                "timestamp": row["timestamp"],
                "alert_type": "RPM Drop Detected",
                "severity": "Medium",
                "message": f"RPM dropped to {row['rpm']}."
            })

        if row["temperature"] > 100:
            alerts.append({
                "timestamp": row["timestamp"],
                "alert_type": "Temperature Spike Detected",
                "severity": "High",
                "message": f"Temperature reached {row['temperature']}°C."
            })

    return alerts