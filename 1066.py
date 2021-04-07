i = 0
positivo = 0
negativo = 0
impar = 0
par = 0
while i < 5:
    n = int(input())
    if n % 2 == 0:
        par += 1
    else:
        impar += 1 

    if n > 0:
        positivo += 1
    elif n != 0:
        negativo += 1
    i += 1

print(par,'valor(es) par(es)')
print(impar,'valor(es) impar(es)')
print(positivo,'valor(es) positivo(s)')
print(negativo,'valor(es) negativo(s)')