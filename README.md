# 💳 Bank Transaction Analysis & Credit Behavior System

## 🚀 Overview

This project simulates real-world credit card behavior by analyzing transaction-level banking data using PostgreSQL, SQL, and Python.

The system tracks:

- Monthly credit card spending
- Next-month repayment behavior
- Outstanding balances
- Interest calculation
- Customer transaction activity

The project combines database-level querying with Python-based data processing to generate financial insights from structured transaction datasets.

---

## 🛠 Tech Stack

- PostgreSQL
- SQL
- Python (Pandas)
- SQLAlchemy
- pgAdmin

---

## 📁 Project Structure

```bash
Banking_Analysis/
│
├── data/
│   └── transactions.csv
│
├── sql/
│   └── credit_analysis.sql
│
├── python/
│   └── data_connect.py
│
├── README.md
```

---

## ⚙️ Features

- Credit card spend tracking
- Repayment mapping using next-month billing logic
- Outstanding balance calculation
- Transaction aggregation and analysis
- PostgreSQL + Python integration
- SQL query execution from external `.sql` files

---

## 🧠 SQL Concepts Used

- CTEs (`WITH`)
- Aggregations (`SUM`, `COUNT`)
- `LEFT JOIN`
- `COALESCE`
- `DATE_TRUNC`
- `INTERVAL`

---

## 🐍 Python Concepts Used

- Pandas DataFrames
- SQLAlchemy database connection
- External SQL query execution
- Data processing and analysis

---

# 📊 Database Setup

## 1️⃣ Create Database

```sql
CREATE DATABASE Bank_analysis;
```

---

## 2️⃣ Create Table

```sql
CREATE TABLE transactions (
    transaction_id INT,
    customer_id INT,
    amount FLOAT,
    transaction_type VARCHAR(20),
    transaction_date DATE,
    merchant VARCHAR(100),
    payment_type VARCHAR(50),
    transaction_category VARCHAR(50)
);
```

---

## 3️⃣ Import CSV

Import `transactions.csv` into PostgreSQL using pgAdmin.

---

# ▶️ How to Run

## 1️⃣ Install Required Libraries

```bash
pip install pandas sqlalchemy psycopg2
```

---

## 2️⃣ Configure PostgreSQL Connection

Update credentials inside:

```bash
python/data_connect.py
```

Example:

```python
engine = create_engine(
    "postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/Bank_analysis"
)
```

---

## 3️⃣ Run Python Script

```bash
cd python
python data_connect.py
```

---

# 📈 Example Analysis

The system analyzes:

- Customer-wise monthly spending
- Repayment behavior
- Outstanding balances
- Transaction frequency
- Overall transaction flow

---

# 💡 Key Learnings

- PostgreSQL integration with Python
- Financial transaction modeling
- SQL-based behavioral analysis
- External SQL query execution
- Data processing using Pandas

---

# 👨‍💻 Author

Prashant Gangwar
