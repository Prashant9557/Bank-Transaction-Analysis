WITH spend AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', transaction_date) AS month,
        SUM(amount) AS total_spend,
        COUNT(*) AS spend_transactions
    FROM transactions
    WHERE transaction_type = 'Debit'
      AND (payment_type = 'CreditCard' OR payment_type = 'DebitCard')
    GROUP BY customer_id, month
),

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

total_txn AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', transaction_date) AS month,
        COUNT(*) AS total_transactions,
        SUM(amount) AS total_amount_flow
    FROM transactions
    GROUP BY customer_id, month
)

SELECT 
    s.customer_id,
    s.month AS spend_month,
    s.total_spend,
    s.spend_transactions,

    COALESCE(r.total_repayment, 0) AS total_repayment,
    COALESCE(r.repayment_transactions, 0) AS repayment_transactions,

    t.total_transactions,
    t.total_amount_flow,

    (s.total_spend - COALESCE(r.total_repayment, 0)) AS outstanding,

    SUM(
    s.total_spend - COALESCE(r.total_repayment, 0)
    )
    OVER (
        PARTITION BY s.customer_id
        ORDER BY s.month
    ) AS running_outstanding

FROM spend s

LEFT JOIN repayment r
ON s.customer_id = r.customer_id
AND r.month = s.month + INTERVAL '1 month'

LEFT JOIN total_txn t
ON s.customer_id = t.customer_id
AND t.month = s.month

ORDER BY s.customer_id, s.month;