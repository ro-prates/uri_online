SELECT empregados.cpf, empregados.enome, departamentos.dnome 
    FROM empregados INNER JOIN departamentos 
        ON empregados.dnumero = departamentos.dnumero 
WHERE empregados.cpf NOT IN (SELECT cpf_emp FROM trabalha)
ORDER BY empregados.cpf