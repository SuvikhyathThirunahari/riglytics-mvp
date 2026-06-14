import {
  FaDatabase,
  FaTachometerAlt,
  FaThermometerHalf,
  FaExclamationTriangle,
  FaCog,
} from "react-icons/fa";

function SummaryCards({ summary, anomalyCount }) {
  if (!summary) {
    return null;
  }

  return (
    <div className="summary-grid">
      <div className="summary-card">
        <div className="card-icon">
          <FaDatabase />
        </div>

        <h3>Total Records</h3>

        <p>{summary.total_records}</p>
      </div>

      <div className="summary-card">
        <div className="card-icon">
          <FaTachometerAlt />
        </div>

        <h3>Average Pressure</h3>

        <p>{summary.average_pressure}</p>
      </div>

      <div className="summary-card">
        <div className="card-icon">
          <FaCog />
        </div>

        <h3>Average RPM</h3>

        <p>{summary.average_rpm}</p>
      </div>

      <div className="summary-card">
        <div className="card-icon">
          <FaThermometerHalf />
        </div>

        <h3>Average Temperature</h3>

        <p>{summary.average_temperature}</p>
      </div>

      <div className="summary-card">
        <div className="card-icon">
          <FaExclamationTriangle />
        </div>

        <h3>Anomalies Found</h3>

        <p>{anomalyCount}</p>
      </div>
    </div>
  );
}

export default SummaryCards;