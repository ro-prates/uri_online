from math import pow

numerador = 3
resultado = 1
i = 1
potencia = 0

while numerador <= 39:
    potencia = pow(2, i)
    resultado += numerador / potencia
    i += 1
    numerador += 2

print(f'{resultado:.2f}')