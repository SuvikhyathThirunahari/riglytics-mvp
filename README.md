# RigLytics Drilling Intelligence MVP

A full-stack drilling intelligence platform that enables users to upload drilling datasets, visualize operational metrics, detect anomalies, and generate alerts through an interactive dashboard.

## Features

* CSV drilling data upload
* Interactive drilling parameter visualization
* Summary metrics dashboard
* Automated anomaly detection
* Alert generation system
* Responsive React frontend
* FastAPI backend APIs
* Cloud deployment using Vercel and Render

## Technology Stack

### Frontend

* React
* Vite
* Axios
* Recharts

### Backend

* FastAPI
* Pandas
* Scikit-Learn

### Deployment

* Vercel (Frontend)
* Render (Backend)

## Architecture

User
↓
React Frontend (Vercel)
↓
FastAPI Backend (Render)
↓
CSV Analytics Engine
├── Summary Metrics
├── Chart Processing
├── Alert Generation
└── Anomaly Detection

## API Endpoints

POST /upload
GET /summary
GET /chart-data
GET /alerts

## Live Demo

Frontend:
https://riglytics-mvp.vercel.app/

Backend:
https://riglytics-api.onrender.com

## Future Improvements

* Real-time drilling data ingestion
* Advanced ML-based anomaly detection
* User authentication
* Historical trend analysis
* Notification integrations
