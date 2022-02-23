controle = 0
soma = 0
continua = 1

while continua != 0:
    n = int(input())
    if n >= 0:
        soma += n
        controle += 1
    else:
        continua = 0

media = soma / controle
print(f'{media:.2f}')