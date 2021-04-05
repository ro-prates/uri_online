numero = float(input())

if numero>100 or numero<0:
    print('Fora de intervalo')
else:
    if numero <= 25:
        print('Intervalo [0,25]')
    elif numero <= 50:
        print('Intervalo (25,50]')
    elif numero <= 75:
        print('Intervalo (50,75]')
    else: print('Intervalo (75,100]')