SELECT customers.id, customers.name 
    FROM customers FULL OUTER JOIN LOCATIONS
        ON customers.id = locations.id_customers
WHERE customers.id NOT IN (SELECT id_customers FROM locations)
ORDER BY customers.id