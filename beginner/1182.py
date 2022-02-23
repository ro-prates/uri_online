matriz = []

numero_coluna = int(input())

operacao = input()

for l in range(12):
    linha = []
    for c in range(12):
        linha.append(float(input()))
    matriz.append(linha)

resultado = 0.0
for i in range(12):
        resultado += matriz[i][numero_coluna]
if operacao == "S":
    print(f'{resultado:.1f}')
elif operacao == "M":
    resultado = resultado / 12
    print(f'{resultado:.1f}')