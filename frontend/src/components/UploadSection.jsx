import { useState } from "react";
import { uploadCSV } from "../services/api";
import toast from "react-hot-toast";

function UploadSection({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      toast.error("Please select a CSV file");
      return;
    }

    try {
      setLoading(true);

      const response = await uploadCSV(file);

      toast.success(
        `Uploaded successfully (${response.rows} records)`
      );

      // Refresh dashboard data automatically
      if (onUploadSuccess) {
        await onUploadSuccess();
      }

      console.log(response);

    } catch (error) {
      console.error(error);
      toast.error("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-card">
      <h2>Upload Drilling Data</h2>

      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={handleUpload}
        disabled={loading}
      >
        {loading ? "Uploading..." : "Upload CSV"}
      </button>
    </div>
  );
}

export default UploadSection;