-- Monthly Credit Card Spend
WITH spend AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', transaction_date) AS month,
        SUM(amount) AS total_spend,
        COUNT(*) AS spend_transactions
    FROM transactions
    WHERE transaction_type = 'Debit'
      AND payment_type = 'CreditCard'
    GROUP BY customer_id, month
),

-- Monthly Repayment (ONLY repayment, not salary)
repayment AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', transaction_date) AS month,
        SUM(amount) AS total_repayment,
        COUNT(*) AS repayment_transactions
    FROM transactions
    WHERE transaction_type = 'Credit'
      AND transaction_category = 'Repayment'
    GROUP BY customer_id, month
),

-- Total transactions (ALL types)
total_txn AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', transaction_date) AS month,
        COUNT(*) AS total_transactions,
        SUM(amount) AS total_amount_flow
    FROM transactions
    GROUP BY customer_id, month
)

-- Final Join
SELECT 
    s.customer_id,
    s.month AS spend_month,

    -- Spend details
    s.total_spend,
    s.spend_transactions,

    -- Repayment details
    COALESCE(r.total_repayment, 0) AS total_repayment,
    COALESCE(r.repayment_transactions, 0) AS repayment_transactions,

    -- Overall activity
    t.total_transactions,
    t.total_amount_flow,

    -- Outstanding
    (s.total_spend - COALESCE(r.total_repayment, 0)) AS outstanding

FROM spend s

LEFT JOIN repayment r
ON s.customer_id = r.customer_id
AND r.month = s.month + INTERVAL '1 month'

LEFT JOIN total_txn t
ON s.customer_id = t.customer_id
AND t.month = s.month

ORDER BY s.customer_id, s.month;