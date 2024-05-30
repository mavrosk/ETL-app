CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS exchange_rates (
    currency_date DATE NOT NULL,
    currency_symbol VARCHAR(3) NOT NULL,
    currency_rate FLOAT NOT NULL,
    PRIMARY KEY (currency_date, currency_symbol)
);
"""

CREATE_MATERIALIZED_VIEW_SQL = """
CREATE MATERIALIZED VIEW IF NOT EXISTS monthly_rates AS
SELECT 
    date_trunc('month', currency_date) AS month,
    currency_symbol,
    MIN(currency_rate) AS min_rate,
    MAX(currency_rate) AS max_rate,
    AVG(currency_rate) AS avg_rate
FROM exchange_rates
GROUP BY month, currency_symbol;
"""

CREATE_VIEW_SQL = """
CREATE VIEW IF NOT EXISTS todays_rates AS
SELECT 
    currency_date,
    currency_symbol,
    currency_rate
FROM exchange_rates
WHERE currency_date = CURRENT_DATE;
"""
