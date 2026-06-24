-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average 1 Year Return
SELECT AVG(return_1yr_pct) AS avg_return_1yr
FROM fact_performance;

-- 3. Average 3 Year Return
SELECT AVG(return_3yr_pct) AS avg_return_3yr
FROM fact_performance;

-- 4. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Top Sharpe Ratio Funds
SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 6. Average NAV
SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 7. Transactions by State
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 8. Total Investment Amount
SELECT SUM(amount_inr) AS total_amount
FROM fact_transactions;

-- 9. KYC Status Distribution
SELECT kyc_status, COUNT(*) AS count
FROM fact_transactions
GROUP BY kyc_status;

-- 10. Fund Count by Category
SELECT category, COUNT(*) AS total_funds
FROM fact_performance
GROUP BY category;