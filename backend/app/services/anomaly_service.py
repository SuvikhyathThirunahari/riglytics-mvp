from sklearn.ensemble import IsolationForest

from app.utils.csv_validator import validate_csv


def detect_anomalies(file_path):
    """
    Detect drilling anomalies using Isolation Forest.
    """

    df = validate_csv(file_path)

    features = df[
        [
            "pressure",
            "rpm",
            "temperature"
        ]
    ]

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    predictions = model.fit_predict(features)

    df["anomaly"] = predictions

    anomaly_rows = df[
        df["anomaly"] == -1
    ]

    return anomaly_rows.to_dict(
        orient="records"
    )