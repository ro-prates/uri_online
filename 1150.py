resultado = 0
contador = 0
x = int(input())
z = int(input())

while z<= x:
    z = int(input())

for i in range(x, z):
    resultado += i
    contador += 1
    if resultado > z:
        break

print(contador)