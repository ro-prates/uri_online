WITH menos AS (
    SELECT divisao.cod_divisao, divisao.nome, SUM(desconto.valor) AS desconto, COUNT(empregado.lotacao_div) AS pessoas 
        FROM divisao INNER JOIN empregado 
            ON divisao.cod_divisao = empregado.lotacao_div
        INNER JOIN emp_desc 
            ON empregado.matr = emp_desc.matr
        INNER JOIN desconto 
            ON emp_desc.cod_desc = desconto.cod_desc
    GROUP BY divisao.cod_divisao, divisao.nome
)

, mais AS(
    SELECT divisao.cod_divisao, divisao.nome, SUM(vencimento.valor) AS salario, COUNT(empregado.lotacao_div) AS pessoas 
        FROM divisao INNER JOIN empregado 
            ON divisao.cod_divisao = empregado.lotacao_div
        INNER JOIN emp_venc 
            ON empregado.matr = emp_venc.matr
        INNER JOIN vencimento 
            ON emp_venc.cod_venc = vencimento.cod_venc
    GROUP BY divisao.cod_divisao, divisao.nome
)

, pessoas AS(
    SELECT lotacao_div, COUNT(lotacao_div) AS quantidade_pessoas FROM empregado
        GROUP BY lotacao_div
    ORDER BY lotacao_div
)

, medias AS (
    SELECT 
        mais.cod_divisao, 
        ROUND(((mais.salario - COALESCE(menos.desconto, 0)) / pessoas.quantidade_pessoas), 2) AS media 
    FROM mais LEFT JOIN menos
	    ON mais.cod_divisao = menos.cod_divisao 
    LEFT JOIN pessoas
        ON mais.cod_divisao = pessoas.lotacao_div
)

, menos_salario AS (
    SELECT 
        empregado.lotacao_div, 
        empregado.matr, 
        empregado.nome, 
        SUM(desconto.valor) AS desconto 
    FROM empregado INNER JOIN emp_desc 
        ON empregado.matr = emp_desc.matr
    INNER JOIN desconto 
        ON emp_desc.cod_desc = desconto.cod_desc
    GROUP BY empregado.matr, empregado.nome, empregado.lotacao_div
)

, mais_salario AS(
    SELECT 
        empregado.lotacao_div, 
        empregado.matr, 
        empregado.nome, 
        SUM(vencimento.valor) AS salario 
    FROM empregado
        INNER JOIN emp_venc 
            ON empregado.matr = emp_venc.matr
        INNER JOIN vencimento 
            ON emp_venc.cod_venc = vencimento.cod_venc
    GROUP BY empregado.matr, empregado.nome, empregado.lotacao_div
)

, salario_final AS(
    SELECT 
        mais_salario.lotacao_div, 
        mais_salario.nome, 
        ROUND((mais_salario.salario - COALESCE(menos_salario.desconto, 0)), 2) AS valor_final 
    FROM mais_salario LEFT JOIN menos_salario 
        ON menos_salario.matr = mais_salario.matr
)

, salariodaspessoas AS(
    SELECT * FROM salario_final
)
 
, mediasdepartamentos AS (
    SELECT * FROM medias
)
  
SELECT 
    departamento.nome AS departamento, 
    divisao.nome AS divisao, 
    mediasdepartamentos.media, 
    MAX(salariodaspessoas.valor_final) AS maior 
FROM divisao 
    INNER JOIN departamento
 	    ON departamento.cod_dep = divisao.cod_dep 
    INNER JOIN mediasdepartamentos 
        ON mediasdepartamentos.cod_divisao = divisao.cod_divisao 
    INNER JOIN salariodaspessoas 
        ON salariodaspessoas.lotacao_div = mediasdepartamentos.cod_divisao
GROUP BY departamento.nome, divisao.nome,  mediasdepartamentos.media
ORDER BY mediasdepartamentos.media DESC