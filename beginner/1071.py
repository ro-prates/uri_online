import sys

n1 = int(input())
n2 = int(input())

if n1 == n2:
    print('0')
    sys.exit(0)
elif n1 < n2:
    menor = n1
    maior = n2
else:
    menor = n2
    maior = n1
    
if menor % 2 == 0:
    menor += 1
else:
    menor += 2
soma = 0
while menor < maior:
    soma += menor
    menor += 2

print(soma)