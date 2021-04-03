n = int(input())
x = []
j = 0

for i in range(1000):
    if j < n:
        x.append(j)
        j += 1
    else:
        j = 0
        x.append(j)
        j += 1

for i in range(1000):
    print(f'N[{i}] = {x[i]}')