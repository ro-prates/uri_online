par = []
impar = []

for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        if len(par) == 5:
            for j in range(5):
                print(f'par[{j}] = {par[j]}')
            par.clear()
    else:
        impar.append(n)
        if len(impar) == 5:
            for j in range(5):
                print(f'impar[{j}] = {impar[j]}')
            impar.clear()
            
for i in range(len(impar)):
    print(f'impar[{i}] = {impar[i]}')

for i in range(len(par)):
    print(f'par[{i}] = {par[i]}')