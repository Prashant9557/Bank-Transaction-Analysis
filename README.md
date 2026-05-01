# Bank-Transaction-Analysis

# 💳 Credit Card Behavior Analysis & Scoring System

## 🚀 Overview

This project simulates real-world credit card usage by analyzing transaction data to track customer spending, repayment behavior, outstanding balances, and generate a basic credit score.

It combines **SQL-based analysis** with **Python (Pandas)** to derive meaningful financial insights.

---

## 🔑 Key Features

- 📊 Monthly credit card spend tracking
- 🔄 Mapping spend with next-month repayment
- 💰 Outstanding balance calculation
- 📈 Interest simulation on unpaid amount
- 🧠 Rule-based credit score generation
- 📉 Transaction-level behavioral analysis

---

## 🛠 Tech Stack

- **Python** (Pandas)
- **SQL** (CTE, Joins, Aggregations)
- **CSV Dataset**

---

---

## 📊 Dataset Description

The dataset contains:

- `customer_id`
- `amount`
- `transaction_type` (Debit/Credit)
- `transaction_date`
- `payment_type` (CreditCard/BankTransfer)
- `transaction_category` (Shopping / Repayment / Salary)

---

## ⚙️ How It Works

1. Tracks **credit card spending (Debit + CreditCard)**
2. Matches it with **next-month repayments**
3. Calculates:
   - Outstanding balance
   - Interest (2%)
4. Generates **credit score** based on:
   - Repayment behavior
   - Spending pattern

---

## ▶️ How to Run (Step-by-Step)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/bank-transaction-credit-scoring.git
cd bank-transaction-credit-scoring


cd python
python credit_analysis.py
```
