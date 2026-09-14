# Naukri Job Analytics

A data engineering and analytics project that scrapes job listings from Naukri, stores the raw data in PostgreSQL, and transforms it into a clean dataset for analysis.

## 🚀 Project Overview

This project demonstrates a simple ETL pipeline:

**Naukri → Selenium → CSV → PostgreSQL → Data Transformation**

The scraper collects job listing information from Naukri and saves it as a CSV file. The CSV data is then loaded into PostgreSQL using Python, where SQL transformations are applied to create a cleaned dataset.

## 🛠️ Tech Stack

- **Python** – Scraping and ETL
- **Selenium** – Web scraping
- **PostgreSQL** – Data storage
- **SQL** – Data transformation
- **Docker** – PostgreSQL containerization
- **pgAdmin** – Database management
- **Git & GitHub** – Version control

## 📂 Project Structure

```text
naukri-job-analytics/
│
├── data/
│   └── jobs.csv
│
├── sql/
│   ├── init.sql
│   └── transformations.sql
│
├── main.py
├── load.py
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md