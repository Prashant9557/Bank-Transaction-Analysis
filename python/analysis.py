import pandas as pd

# Load data
df = pd.read_csv('../data/transactions.csv')
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Create month column
df['month'] = df['transaction_date'].dt.to_period('M')

# -------------------------------
# 1. Credit Card Spend
# -------------------------------
spend = df[(df['transaction_type'] == 'Debit') & 
           (df['payment_type'] == 'CreditCard')] \
    .groupby(['customer_id', 'month']) \
    .agg(
        total_spend=('amount', 'sum'),
        spend_transactions=('amount', 'count')
    ).reset_index()

# -------------------------------
# 2. Repayment (ONLY repayment)
# -------------------------------
repayment = df[(df['transaction_type'] == 'Credit') & 
               (df['transaction_category'] == 'Repayment')] \
    .groupby(['customer_id', 'month']) \
    .agg(
        total_repayment=('amount', 'sum'),
        repayment_transactions=('amount', 'count')
    ).reset_index()

# Shift repayment month back (M+1 → M)
repayment['month'] = repayment['month'] - 1

# -------------------------------
# 3. Total Transactions
# -------------------------------
total_txn = df.groupby(['customer_id', 'month']) \
    .agg(
        total_transactions=('amount', 'count'),
        total_amount_flow=('amount', 'sum')
    ).reset_index()

# -------------------------------
# 4. Merge all
# -------------------------------
merged = pd.merge(spend, repayment, 
                  on=['customer_id', 'month'], 
                  how='left')

merged = pd.merge(merged, total_txn,
                  on=['customer_id', 'month'],
                  how='left')

# Fill NaN values
merged['total_repayment'] = merged['total_repayment'].fillna(0)
merged['repayment_transactions'] = merged['repayment_transactions'].fillna(0)

# -------------------------------
# 5. Outstanding
# -------------------------------
merged['outstanding'] = merged['total_spend'] - merged['total_repayment']

# -------------------------------
# 6. Interest (2%)
# -------------------------------
merged['interest'] = merged['outstanding'].apply(lambda x: x * 0.02 if x > 0 else 0)

# -------------------------------
# 7. Credit Score Logic
# -------------------------------
def calculate_score(row):
    score = 600

    if row['total_repayment'] >= row['total_spend']:
        score += 30
    elif row['total_repayment'] > 0:
        score += 10
    else:
        score -= 20

    # High usage penalty
    if row['total_spend'] > 1500:
        score -= 10

    return score

merged['credit_score'] = merged.apply(calculate_score, axis=1)

# -------------------------------
# 8. Extra Metrics
# -------------------------------
merged['avg_transaction_size'] = merged['total_amount_flow'] / merged['total_transactions']
merged['repayment_ratio'] = merged['total_repayment'] / merged['total_spend']

# -------------------------------
# 9. Output
# -------------------------------
print("\n📊 Final Credit Analysis:\n")
print(merged)