n = int(input())
x = []

x = input().split()

menor = int(x[0])
posicao = 0

for i in range(1, n):
    if menor > int(x[i]):
        menor = int(x[i])
        posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')