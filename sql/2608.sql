SELECT categories.name, SUM(products.amount) AS sum 
    FROM categories INNER JOIN products 
        ON products.id_categories = categories.ID
GROUP BY categories.name