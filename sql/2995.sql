SELECT 
    packages.year, 
    u1.name AS sender, u2.name AS receiver 
FROM packages
    INNER JOIN users u1
	    ON packages.id_user_sender = u1.id
    INNER JOIN users u2
        ON packages.id_user_receiver = u2.id
WHERE (color = 'blue' OR YEAR = 2015) AND u2.address <> 'Taiwan'
ORDER BY year DESC