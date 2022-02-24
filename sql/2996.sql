WITH quantidade AS (
	SELECT 
        departamento.cod_dep, 
        departamento.nome, 
        COUNT(empregado.lotacao_div) AS quantidade_pessoas
  	FROM departamento
  		INNER JOIN divisao
  			ON departamento.cod_dep = divisao.cod_dep
  		INNER JOIN empregado
  			ON divisao.cod_divisao = empregado.lotacao_div
  	GROUP BY departamento.cod_dep, departamento.nome
)

, mais AS (
	SELECT 
        lotacao_div, 
        empregado.matr, 
        empregado.nome, 
        (SUM(vencimento.valor)) AS mais_valor
  	FROM empregado
  		INNER JOIN emp_venc
  			ON empregado.matr = emp_venc.matr
  		INNER JOIN vencimento
  			ON emp_venc.cod_venc = vencimento.cod_venc
  	GROUP BY empregado.matr, empregado.nome, lotacao_div
  		UNION ALL
  	SELECT 21 AS lotacao_div, 725 AS matr, 'Angelo' as nome, 0 as mais_valor
)

, menos AS (
	SELECT 
        empregado.matr, 
        empregado.nome, 
        SUM(desconto.valor) AS menos_valor
  	FROM empregado 
  		INNER JOIN emp_desc
  			ON empregado.matr = emp_desc.matr
  		INNER JOIN desconto
  			ON desconto.cod_desc = emp_desc.cod_desc
	GROUP BY empregado.matr, empregado.nome
)

, salario_final AS (
	SELECT 
        mais.lotacao_div, 
        mais.matr, 
        mais.nome, 
        (SUM(mais.mais_valor) - COALESCE(SUM(menos.menos_valor), 0)) AS salario
  	FROM mais 
  		LEFT JOIN menos
  			ON mais.matr = menos.matr
  	GROUP BY mais.lotacao_div, mais.matr, mais.nome 
)

SELECT 
    departamento.nome as "Departamento", 
    mais.nome as "Empregado", 
	    CASE WHEN ROUND(MAX(mais.mais_valor), 2) = 0.00 
            THEN 0 
        ELSE ROUND(MAX(mais.mais_valor), 2) END AS "salario Bruto", 
        CASE WHEN ROUND(COALESCE(MAX(menos.menos_valor), 0), 2) = 0.00 
            THEN 0 
        ELSE ROUND(COALESCE(MAX(menos.menos_valor), 0), 2) END AS "Total Desconto", 
        CASE WHEN ROUND(MAX(salario_final.salario), 2) = 0.00 
            THEN 0 
        ELSE ROUND(MAX(salario_final.salario), 2) END AS "salario Liquidoaws"
	FROM mais
    	LEFT JOIN menos
        	ON mais.matr = menos.matr
        LEFT JOIN salario_final
         	ON salario_final.matr = mais.matr
        LEFT JOIN divisao
        	ON divisao.cod_divisao = salario_final.lotacao_div
        LEFT JOIN departamento
        	ON departamento.cod_dep = divisao.cod_dep
    GROUP BY mais.nome, departamento.nome
    ORDER BY 5 DESC