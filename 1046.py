a, b = input().split(" ")

a = int(a)
b = int(b)

if a == b:
    print('O JOGO DUROU 24 HORA(S)')
elif a < b:
    horas = b - a
    print('O JOGO DUROU', horas,'HORA(S)')
else:
    resultado1 = 24 - a
    final = resultado1 + b
    print('O JOGO DUROU', final,'HORA(S)')