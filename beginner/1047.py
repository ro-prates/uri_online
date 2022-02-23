hora1, minuto1, hora2, minuto2 = input().split(" ")

hora1 = int(hora1)
minuto1 = int(minuto1)
hora2 = int(hora2)
minuto2 = int(minuto2)

if hora1 == hora2 and minuto1 == minuto2:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif hora1 == hora2:
    if minuto1 < minuto2:
        resultado = minuto2 - minuto1
        print('O JOGO DUROU 0 HORA(S) E',resultado, 'MINUTO(S)')
    else:
        resultado = (60 - minuto1) + minuto2
        print('O JOGO DUROU 23 HORA(S) E',resultado, 'MINUTO(S)')
elif hora1 < hora2:
    if minuto1 < minuto2:
        hora = hora2 - hora1
        minuto = minuto2 - minuto1
        print('O JOGO DUROU',hora,'HORA(S) E',minuto, 'MINUTO(S)')
    elif minuto1 == minuto2:
        hora = hora2 - hora1
        print('O JOGO DUROU',hora,'HORA(S) E 0 MINUTO(S)')
    else:
        hora = hora2 - hora1 - 1
        minuto = 60 - minuto1 + minuto2
        print('O JOGO DUROU',hora,'HORA(S) E',minuto, 'MINUTO(S)')
else:
    if minuto1 == minuto2:
        hora = 24 - hora1 + hora2
        print('O JOGO DUROU',hora,'HORA(S) E 0 MINUTO(S)')
    elif minuto1 > minuto2:
        hora = 24 - hora1 + hora2 - 1
        minuto = 60 - minuto1 + minuto2
        print('O JOGO DUROU',hora,'HORA(S) E',minuto, 'MINUTO(S)')
    else:
        minuto = minuto2 - minuto1
        hora = 24 - hora1 + hora2
        print('O JOGO DUROU',hora,'HORA(S) E',minuto, 'MINUTO(S)')