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

# Print result
print(df)