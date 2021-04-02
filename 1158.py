n = int(input())
resultado = 0

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)

    if x % 2 != 0:
        for j in range(y):
            resultado += x
            x += 2
        print(resultado)
        resultado = 0
    else:
        x += 1
        for j in range(y):
            resultado += x
            x += 2
        print(resultado)
        resultado = 0