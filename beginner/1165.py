n = int(input())
soma = 0
for i in range(n):
    numero = int(input())
    for j in range(1, numero+1):
        if numero % j == 0:
            soma += 1
        
    if soma == 2:
        print(f'{numero} eh primo')
    else:
        print(f'{numero} nao eh primo')
    soma = 0