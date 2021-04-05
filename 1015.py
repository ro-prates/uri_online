x1,y1 = input().split(" ")
x2,y2 = input().split(" ")
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

primeiro = x2 - x1
segundo = y2 - y1

terceiro = pow(primeiro,2) + pow(segundo,2)
resultado = pow(terceiro,0.5)

print('{0:.4f}'.format(resultado))