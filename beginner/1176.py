n0 = 0
n1 = 1
soma = 1
x = []

x.append(n0)
x.append(n1)

for i in range(60):
    n1 = soma
    soma = n0 + n1
    n0 = n1
    x.append(soma)

n = int(input())
for i in range(n):
    numero = int(input())
    print(f'Fib({numero}) = {x[numero]}')