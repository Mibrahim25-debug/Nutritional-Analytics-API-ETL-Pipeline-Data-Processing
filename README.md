# Nutritional-Analytics-API-ETL-Pipeline-Data-Processing

**Author:** Ibrahim Awan  
**Role:** Data Analyst & Backend Developer  

## 📌 Project Overview
The Nutritional Analytics API is a high-performance backend system designed to bridge data engineering with web serving. This project acts as an automated ETL (Extract, Transform, Load) pipeline. It programmatically connects to the public OpenFoodFacts database, extracts raw JSON data regarding food products, performs mathematical vectorization to analyze protein density, and serves the cleaned, analyzed dataset via a RESTful API endpoint.

## 🛠️ Technical Architecture & Tech Stack
* **Web Framework:** FastAPI (Python)
* **Server Engine:** Uvicorn (ASGI)
* **Data Analysis:** Pandas
* **Network Requests:** Python `requests` library

## ⚙️ Core Features
1.  **Automated Data Extraction:** Executes synchronous HTTP GET requests to third-party endpoints to ingest unstructured JSON payloads.
2.  **In-Memory Data Transformation:** Utilizes the Pandas library to convert standard Python arrays into DataFrames, handling missing values and filtering null data.
3.  **Algorithmic Sorting:** Calculates a custom `protein_per_calorie` ratio using vectorized mathematical operations, sorting the dataset for maximum nutritional value.
4.  **Optimized Delivery:** Serializes the complex Pandas DataFrame back into a standard JSON response for immediate client consumption
