from app.utils.csv_validator import validate_csv


def detect_anomalies(file_path):
    """
    Rule-based drilling anomaly detection.
    """

    df = validate_csv(file_path)

    anomalies = []

    for _, row in df.iterrows():

        reasons = []

        if row["pressure"] > 4200:
            reasons.append("High Pressure")

        if row["rpm"] < 90:
            reasons.append("Low RPM")

        if row["temperature"] > 110:
            reasons.append("High Temperature")

        if reasons:

            anomaly = row.to_dict()

            anomaly["reason"] = ", ".join(reasons)

            anomalies.append(anomaly)

    return anomalies