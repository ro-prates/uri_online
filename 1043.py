a, b, c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

sub1 = b - c
if sub1 < 0:
    sub1 = sub1 * (-1)

sub2 = a - c
if sub2 < 0:
    sub2 = sub2 * (-1)

sub3 = a - b
if sub3 < 0:
    sub3 = sub3 * (-1)


if sub1 < a and a < (b+c) and sub2 < b and b < (a+c) and sub3 < c and c < (a+b):
    perimetro = a+b+c
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    area = c * (a + b) / 2
    print('Area = {:.1f}'.format(area))