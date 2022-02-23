x = []

n = float(input())

x.append(n)

for i in range(99):
    n /= 2
    x.append(n)

for i in range(100):
    print(f'N[{i}] = {x[i]:.4f}')