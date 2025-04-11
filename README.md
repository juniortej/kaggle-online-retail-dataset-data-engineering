# 🛍️ Online Retail Data Engineering Pipeline

This project implements a complete data engineering pipeline for the Online Retail Dataset from Kaggle. It includes data ingestion, transformation, and modeling steps to support comprehensive analysis of retail transactions.

---

## 📦 Dataset Overview

The dataset consists of nearly a year's worth of transactional data from a UK-based online retailer, containing:

- Invoice numbers
- Stock codes
- Product descriptions
- Quantities and prices
- Invoice timestamps
- Customer IDs
- Country of purchase

---

## 🧰 Project Architecture

```plaintext
+-------------------+
|   Data Source     |
| Kaggle Retail CSV |
+-------------------+
         |
         v
+-----------------------+
| Data Ingestion Layer  |
| (Pandas CSV Loader)   |
+-----------------------+
         |
         v
+-----------------------+
| Data Transformation   |
| (Pandas DataFrames)   |
+-----------------------+
         |
         v
+-----------------------+
| Data Modeling         |
| (Star Schema Design)  |
+-----------------------+
         |
         v
+-----------------------+
| Data Analysis         |
| (Exploratory Insights)|
+-----------------------+
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Pandas
- Jupyter Notebook (optional, for exploration)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/juniortej/kaggle-online-retail-dataset-data-engineering.git
cd kaggle-online-retail-dataset-data-engineering
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Download dataset:**

- Visit: [Kaggle Dataset](https://www.kaggle.com/datasets/carrie1/ecommerce-data)
- Download `data.csv` and move it into the `/data` directory of this project

---

## 🗂️ Project Structure

```plaintext
├── common_tools/        # Utility functions
├── config/              # Configuration files
├── data-modeling/       # Schema design and transformations
├── etl/                 # ETL pipeline scripts
├── ingestion/           # Data loading scripts
├── workflow/            # Orchestration logic (if used)
├── data/                # Raw dataset goes here
├── requirements.txt     # Dependencies
├── README.md            # You're reading this!😁
```

---

## 📊 Analytical Goals

- Track top-selling products
- Identify purchase patterns by country
- Understand customer purchasing frequency
- Visualize revenue trends over time

---

## 📈 Future Enhancements

- Data validation checks
- Data warehouse integration
- Dashboard integration (Tableau, Power BI)
- Scheduled pipelines using Airflow or Prefect (I did with prefect directly on it)

---

## 🤝 Contributions

Contributions are welcome! Please open issues or submit a pull request for any feature enhancements or bug fixes.

---
