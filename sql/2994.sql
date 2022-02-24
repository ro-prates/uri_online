SELECT 
    temperature, 
    COUNT(*) AS number_of_records FROM records
GROUP by temperature, mark
ORDER by MIN(id)