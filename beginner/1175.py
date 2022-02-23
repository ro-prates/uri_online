x = []
j = 19
for i in range(20):
    x.append(int(input()))
for i in range(20):
    print(f'N[{i}] = {x[j]}')
    j -= 1