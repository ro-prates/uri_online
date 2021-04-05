a, b = input().split(" ")

a = int(a)
b = int(b)

if a < b and (b // a) * a == b:
    print('Sao Multiplos')
elif b < a and (a // b) * b == a:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')  