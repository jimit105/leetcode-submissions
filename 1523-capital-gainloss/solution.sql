SELECT stock_name, SUM(
    CASE
        WHEN operation='BUY' THEN -price
        ELSE price
    END
) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
