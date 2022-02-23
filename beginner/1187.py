matriz = []

operacao = input()

for l in range(12):
    linha = []
    for c in range(12):
        linha.append(float(input()))
    matriz.append(linha)

resultado = 0.0
controle1 = 0
controle2 = 11
for l in range(12):
    for c in range(12):
        if c > controle1 and c < controle2:
            resultado += matriz[l][c]
    controle1 += 1   
    controle2 -= 1   
if operacao == "S" or operacao == "s":
    print(f'{resultado:.1f}')
elif operacao == "M" or operacao == "m":
    resultado = resultado / 30
    print(f'{resultado:.1f}')