SELECT name, char_length(name) as length 
    FROM people
ORDER BY char_length(name) DESC