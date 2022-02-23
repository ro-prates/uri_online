controle = 1

while controle != 0:
    resultado = 0
    n = int(input())
    if n != 0:
        if n % 2 == 0:
            for j in range(5):
                resultado += n
                n += 2
            print(resultado)
        else:
            n += 1
            for j in range(5):
                resultado += n
                n += 2
            print(resultado)
    else:
        controle = 0