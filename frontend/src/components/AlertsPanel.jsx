function AlertsPanel({ alerts }) {
  if (!alerts || alerts.length === 0) {
    return null;
  }

  return (
    <div className="alerts-card">
      <h2>Drilling Alerts</h2>

      <table className="alerts-table">
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Severity</th>
            <th>Alert Type</th>
            <th>Message</th>
          </tr>
        </thead>

        <tbody>
          {alerts.map((alert, index) => (
            <tr key={index}>
              <td>{alert.timestamp}</td>

              <td>
                <span
                  className={
                    alert.severity === "High"
                      ? "severity-high"
                      : "severity-medium"
                  }
                >
                  {alert.severity}
                </span>
              </td>

              <td>{alert.alert_type}</td>

              <td>{alert.message}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AlertsPanel;