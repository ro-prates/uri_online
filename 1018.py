quantidade = int(input())
valor = quantidade
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0
n100 = quantidade//100
if n100>0:
    quantidade = quantidade-100*n100
n50 = quantidade//50
if n50>0:
    quantidade = quantidade-50*n50
n20 = quantidade//20
if n20>0:
    quantidade = quantidade-20*n20
n10 = quantidade//10
if n10>0:
    quantidade = quantidade-10*n10
n5 = quantidade//5
if n5>0:
    quantidade = quantidade-5*n5
n2 = quantidade//2
if n2>0:
    quantidade = quantidade-2*n2

print(valor)
print(n100,'nota(s) de R$ 100,00')
print(n50,'nota(s) de R$ 50,00')
print(n20,'nota(s) de R$ 20,00')
print(n10,'nota(s) de R$ 10,00')
print(n5,'nota(s) de R$ 5,00')
print(n2,'nota(s) de R$ 2,00')
print(quantidade,'nota(s) de R$ 1,00')