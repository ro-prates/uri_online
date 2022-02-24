WITH temp AS (
	SELECT 
        client_id, 
        month, 
        SUM(profit) OVER (PARTITION BY client_id ORDER BY month) AS "cumulativo" 
    FROM operations
)

, filtro AS (
	SELECT 
        clients.name, 
        clients.investment, 
        month,
        cumulativo 
    FROM temp INNER JOIN clients ON clients.id = temp.client_id 
    WHERE cumulativo >= clients.investment
)

SELECT 
    name, 
    min(investment) AS investment, 
    min(month) AS month_of_payback, 
    min(cumulativo - investment) AS return  
FROM filtro
    GROUP BY name
    ORDER BY return desc