import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Qwertyui%401234567@localhost:5432/Bank_analysis"
)

# SQL Query
query = open("../sql/credit_analysis.sql", "r").read()

# Run query
df = pd.read_sql(query, engine)

# Credit Score Logic
# -----------------------------------

def calculate_credit_score(row):

    score = 600

    # Full repayment
    if row['total_repayment'] >= row['total_spend']:
        score += 50

    # Partial repayment
    elif row['total_repayment'] > 0:
        score += 20

    # No repayment
    else:
        score -= 50

    # High outstanding penalty
    if row['outstanding'] > 1000:
        score -= 30

    return max(300, min(score, 900))


# Apply score calculation
df['credit_score'] = df.apply(calculate_credit_score, axis=1)

# -----------------------------------
# Display Final Output
# -----------------------------------

print("\n📊 Final Credit Analysis:\n")
print(df)

# # Print result
# print(df)