a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

delta = pow(b,2)-4*a*c
denominador = 2*a
if delta < 0 or denominador == 0:
    print('Impossivel calcular')
else:
    raiz = pow(delta,0.5)
    x1 = (-b+raiz)/denominador
    x2 = (-b-raiz)/denominador
    print('R1 = {0:.5f}'.format(x1))
    print('R2 = {0:.5f}'.format(x2))