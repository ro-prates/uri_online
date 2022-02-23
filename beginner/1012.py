a,b,c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)
triangulo = a*c/2
circulo = 3.14159*pow(c,2)
trapezio = (a+b)*c/2
quadrado = b*b
retangulo = a*b
print('TRIANGULO: {0:.3f}'.format(triangulo))
print('CIRCULO: {0:.3f}'.format(circulo))
print('TRAPEZIO: {0:.3f}'.format(trapezio))
print('QUADRADO: {0:.3f}'.format(quadrado))
print('RETANGULO: {0:.3f}'.format(retangulo))