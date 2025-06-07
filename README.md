# 🧠 Sales Copilot Lakehouse
[![Built with Python](https://img.shields.io/badge/Built%20with-Python-blue?logo=python)](https://www.python.org/)
[![Powered by Spark](https://img.shields.io/badge/Data%20Migration-Spark-orange?logo=apache-spark)](https://spark.apache.org/)
[![dbt Models](https://img.shields.io/badge/Data%20Modeling-dbt-red?logo=dbt)](https://www.getdbt.com/)
[![Streamlit App](https://img.shields.io/badge/UI-Streamlit-lightgrey?logo=streamlit)](https://streamlit.io/)
[![RAG LLM](https://img.shields.io/badge/LLM-RAG-green?logo=openai)]()

A full-stack AI assistant built for querying EV product knowledge, powered by a robust Data Engineering pipeline and Retrieval-Augmented Generation (RAG).

> ✅ Designed as a **portfolio project for Data Engineer roles**, integrating batch processing, modeling, BI reporting, and AI-based interaction.

---

## 📸 Project Overview

> 🚗 Use case: Empower sales teams to interact with EV product & sales data via natural language.

![Project Architecture Diagram](./images/architecture.png) <!-- Add your image later -->

---

## 🧰 Tech Stack

| Layer             | Tools / Frameworks                                           |
|------------------|--------------------------------------------------------------|
| **Data Ingestion** | Apache Spark (PySpark) + MinIO (S3 API)                      |
| **Transformation**| dbt (data modeling, pipeline orchestration)                  |
| **Data Warehouse**| DuckDB (local), or replaceable with Redshift/Snowflake       |
| **BI Dashboard**  | Apache Superset (sales insights, color/model analysis)       |
| **Embedding Store**| Chroma (local vector DB)                                    |
| **LLM Backend**   | Ollama + Mistral + nomic-embed-text                          |
| **UI Layer**      | Streamlit chatbot                                            |
| **Ops / Dev Tooling** | Ngrok, Python, dotenv, logging                           |

---

## 📊 Data Pipeline Walkthrough

### 1. 🔁 Data Migration with Spark

- Used **PySpark** to extract, clean, and load raw sales data into a lakehouse.
- Integrated with **MinIO** as a low-cost S3 alternative for object storage.

```bash
# Sample code snippet
df = spark.read.csv("s3a://lakehouse/sales.csv", header=True)
df.write.parquet("s3a://lakehouse/processed/")
```
📷 Screenshot: Spark Job in Terminal (TO ADD)

### 2. 🧱 Data Modeling with dbt
	•	Created models for products, sales_summary, and color_distribution.
	•	Scheduled and tested transformations locally.
```sql
-- Example dbt model
SELECT 
    model,
    color,
    COUNT(*) AS sales_count
FROM {{ ref('sales') }}
GROUP BY 1, 2

```
📷 Screenshot: dbt DAG and dbt run logs (TO ADD)

### 3. 📈 Dashboard with Apache Superset
	•	Built an interactive dashboard to analyze:
	•	Most sold EV colors
	•	Region-wise model distribution
	•	Temporal sales trends

📷 Screenshot: Superset Dashboard (TO ADD)

### 4. 🔍 Embedding + Vector Search (Chroma)
	•	Loaded all markdown & product PDFs
	•	Used nomic-embed-text for document embeddings via Ollama
	•	Stored vector chunks in a local Chroma DB

📷 Screenshot: Chroma DB files created (TO ADD)
🧠 Example Query

“What colors is the AeroFlow model available in?”

Chatbot Response:
The AeroFlow model is available in Red, Glacier Blue, and Pearl White.

With sources retrieved from embedded markdown/PDF documentation.

##  Architecture Summary
```mermaid
flowchart TD
    A[Raw CSV / Docs] --> B[Apache Spark]
    B --> C[MinIO / S3]
    C --> D[dbt Modeling]
    D --> E[DuckDB / Warehouse]
    E --> F[Superset Dashboards]
    C --> G[LangChain + Embedding]
    G --> H[Chroma Vector Store]
    H --> I[Ollama (LLM)]
    I --> J[Streamlit Chatbot]
```
## 🎯 Skills Demonstrated
	•	✅ PySpark for large-scale transformation
	•	✅ dbt for data modeling & CI-friendly pipelines
	•	✅ Superset for rapid BI development
	•	✅ LLM apps using LangChain + Ollama + Chroma
	•	✅ Streamlit for frontend chatbot UI
	•	✅ Environment control with .env, pyenv, ngrok

## 📎 Next Steps
	•	Add PostgreSQL or Snowflake as production DWH
	•	Deploy chatbot publicly with Docker + Ngrok
	•	Add session memory and multi-turn RAG
## 📁 Repository Structure
<pre><code>Sales-Copilot-Lakehouse/
├── rag/                    # LLM, RAG, Chatbot code
│   ├── manage_chroma_db.py
│   ├── streamlit_chat.py
├── dbt/                    # dbt models and config
│   ├── models/
│   ├── dbt_project.yml
├── spark_jobs/            # PySpark scripts for ingestion
├── superset/              # Superset dashboard exports
├── chroma/                # Persisted vector DB
├── images/                # 📷 Screenshot placeholders
├── .env                   # Environment secrets
└── README.md              # You're here
</code></pre>

