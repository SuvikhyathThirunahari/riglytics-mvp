import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

/*
|--------------------------------------------------------------------------
| Upload CSV
|--------------------------------------------------------------------------
*/

export const uploadCSV = async (file) => {
  const formData = new FormData();

  formData.append("file", file);

  const response = await API.post(
    "/upload-csv",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};

/*
|--------------------------------------------------------------------------
| Summary Metrics
|--------------------------------------------------------------------------
*/

export const getSummary = async () => {
  const response = await API.get("/summary");
  return response.data;
};

export const getChartData = async () => {
  const response = await API.get("/chart-data");
  return response.data;
};
export const getAlerts = async () => {
  const response = await API.get("/alerts");
  return response.data;
};
export const getAnomalies = async () => {
  const response = await API.get("/anomalies");
  return response.data;
};
export default API;