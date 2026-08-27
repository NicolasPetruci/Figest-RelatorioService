# 📈 Figest-RelatorioService

> ⚠️ **Educational Project Notice**: This service is part of the **Figest** financial ecosystem, created for study, research, and testing purposes to demonstrate Python FastAPI data processing and document generation.

---

## 📌 Overview

**Figest-RelatorioService** is a Python-based reporting engine. It processes financial data, aggregates monthly/annual trends using Pandas, and generates downloadable documents including PDF reports, CSV spreadsheets, and chart images.

---

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Framework:** FastAPI + Uvicorn
* **Data Processing:** Pandas
* **PDF Generation:** ReportLab
* **Chart Rendering:** Plotly

---

## 📄 Export & Report Endpoints

| Method | Endpoint | Media Type | Description |
|---|---|---|---|
| `GET` | `/exports/pdf` | `application/pdf` | Generate printable PDF financial report |
| `GET` | `/exports/csv` | `text/csv` | Export raw transaction table to CSV |
| `GET` | `/exports/chart` | `image/png` | Render PNG image of expense distribution |
| `GET` | `/reports/monthly` | `application/json` | JSON summary for specific month/year |

---

## 🚀 Running Locally

```bash
python -m venv .venv
source .venv/bin/activate # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --port 3004 --reload
```
