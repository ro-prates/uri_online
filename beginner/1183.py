matriz = []

operacao = input()

for l in range(12):
    linha = []
    for c in range(12):
        linha.append(float(input()))
    matriz.append(linha)

resultado = 0.0
for l in range(12):
    for c in range(12):
        if c > l:
            resultado += matriz[l][c]   
if operacao == "S" or operacao == "s":
    print(f'{resultado:.1f}')
elif operacao == "M" or operacao == "m":
    resultado = resultado / 66
    print(f'{resultado:.1f}')