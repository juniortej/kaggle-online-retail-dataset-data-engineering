# 🛒 Kaggle Online Retail Dataset Analysis

This project performs data ingestion, cleaning, and exploratory data analysis on the Kaggle Online Retail Dataset. It demonstrates a professional data engineering pipeline using Python and Pandas.

---

## 📐 Architecture Overview

```plaintext
             +-------------------+
             |   Data Source     |
             | Kaggle Retail CSV |
             +-------------------+
                      |
                      v
       +----------------------------+
       |    Data Ingestion Layer    |
       | (load from CSV with Pandas)|
       +----------------------------+
                      |
                      v
       +----------------------------+
       |    Data Cleaning Layer     |
       | - Remove nulls             |
       | - Filter bad records       |
       +----------------------------+
                      |
                      v
       +----------------------------+
       |      Feature Engineering   |
       | - Total Price column       |
       | - DateTime features        |
       +----------------------------+
                      |
                      v
       +----------------------------+
       | Exploratory Data Analysis  |
       | - Charts with Seaborn      |
       | - Summary Stats            |
       +----------------------------+

kaggle-online-retail-dataset/
│
├── data/
│   └── OnlineRetail.csv              # Original dataset (downloaded from Kaggle)
│
├── notebooks/
│   └── online_retail_analysis.ipynb  # Main EDA notebook
│
├── src/
│   ├── data_loader.py                # Data loading logic
│   ├── data_cleaner.py               # Cleaning functions
│   └── feature_engineer.py           # Feature engineering
│
├── tests/
│   └── test_data_cleaner.py          # Unit tests
│
├── requirements.txt
└── README.md
```

## Setup Instructions
### 1. Clone & Install Dependencies
```
git clone https://github.com/juniortej/kaggle-online-retail-dataset.git
cd kaggle-online-retail-dataset
```

## Optional: Create virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
```
## Install dependencies
pip install -r requirements.txt
```

## Features
✅ Load raw transactional retail data

🧹 Clean dataset: drop nulls, remove negative quantities/prices

💡 Add features like TotalPrice and InvoiceMonth

📊 Visualize total monthly sales and top-selling items


🧠 Data Fields

- InvoiceNo: Transaction ID

- StockCode: Product ID

- Description: Product Name

- Quantity: Number of units sold

- InvoiceDate: Date and time of transaction

- UnitPrice: Price per unit

- CustomerID: ID of the customer

- Country: Customer location

## 📜 License
This project is licensed under the MIT License.

