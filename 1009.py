nome = input()
salario = float(input())
vendas = float(input())

resultado = salario + 0.15 * vendas

print('TOTAL = R$ {0:.2f}'.format(resultado))