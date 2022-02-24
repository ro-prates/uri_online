SELECT customers.name, rentals.rentals_date 
    FROM customers INNER JOIN rentals 
        ON rentals.id_customers = customers.ID
WHERE EXTRACT(MONTH FROM (rentals.rentals_date)) = '9'