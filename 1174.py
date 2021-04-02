x = []

for i in range(100):
    x.append(float(input()))

for i in range(100):
    if x[i] <= 10:
        print(f'A[{i}] = {x[i]:.1f}')