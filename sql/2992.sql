SELECT amount FROM value_table
    GROUP by amount
    ORDER BY count(amount) DESC
LIMIT 1