SELECT name, ROUND((10*salary/100), 2) AS tax 
    FROM people
WHERE salary >= 3000