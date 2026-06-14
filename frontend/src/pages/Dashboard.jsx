import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import UploadSection from "../components/UploadSection";
import SummaryCards from "../components/SummaryCards";
import ChartsSection from "../components/ChartsSection";
import AlertsPanel from "../components/AlertsPanel";

import {
  getSummary,
  getChartData,
  getAlerts,
  getAnomalies,
} from "../services/api";

function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [chartData, setChartData] = useState([]);
  const [alerts, setAlerts] = useState([]);
  const [anomalies, setAnomalies] = useState([]);

  const loadDashboardData = async () => {
    try {
      const [
        summaryData,
        chartDataData,
        alertsData,
        anomaliesData,
      ] = await Promise.all([
        getSummary(),
        getChartData(),
        getAlerts(),
        getAnomalies(),
      ]);

      setSummary(summaryData);
      setChartData(chartDataData);
      setAlerts(alertsData);
      setAnomalies(anomaliesData);

    } catch (error) {
      console.error(
        "Dashboard Load Error:",
        error
      );
    }
  };

  useEffect(() => {
    loadDashboardData();
  }, []);

  return (
    <div>
      <Navbar />

      <div className="dashboard-container">

        <UploadSection
          onUploadSuccess={loadDashboardData}
        />

        <h2 className="section-title">
          Operational Overview
        </h2>

        <SummaryCards
          summary={summary}
          anomalyCount={anomalies.length}
        />

        <h2 className="section-title">
          Drilling Trends
        </h2>

        <ChartsSection data={chartData} />

        <h2 className="section-title">
          Operational Alerts
        </h2>

        <AlertsPanel alerts={alerts} />

      </div>
    </div>
  );
}

export default Dashboard;