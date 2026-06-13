from app.utils.csv_validator import validate_csv


def get_chart_data(file_path):
    """
    Return drilling data formatted for charts.
    """

    df = validate_csv(file_path)

    return df.to_dict(
        orient="records"
    )