salario = float(input())

if salario <= 400:
    reajuste = 15
    novo_salario = (salario * reajuste /100) + salario
    ganho = novo_salario - salario
    print('Novo salario: {:.2f}'.format(novo_salario))
    print('Reajuste ganho: {:.2f}'.format(ganho))
    print('Em percentual: {:.0f} %'.format(reajuste))
elif salario <= 800:
    reajuste = 12
    novo_salario = (salario * reajuste /100) + salario
    ganho = novo_salario - salario
    print('Novo salario: {:.2f}'.format(novo_salario))
    print('Reajuste ganho: {:.2f}'.format(ganho))
    print('Em percentual: {:.0f} %'.format(reajuste))
elif salario <= 1200:
    reajuste = 10
    novo_salario = (salario * reajuste /100) + salario
    ganho = novo_salario - salario
    print('Novo salario: {:.2f}'.format(novo_salario))
    print('Reajuste ganho: {:.2f}'.format(ganho))
    print('Em percentual: {:.0f} %'.format(reajuste))
elif salario <= 2000:
    reajuste = 7
    novo_salario = (salario * reajuste /100) + salario
    ganho = novo_salario - salario
    print('Novo salario: {:.2f}'.format(novo_salario))
    print('Reajuste ganho: {:.2f}'.format(ganho))
    print('Em percentual: {:.0f} %'.format(reajuste))
elif salario > 2000:
    reajuste = 4
    novo_salario = (salario * reajuste /100) + salario
    ganho = novo_salario - salario
    print('Novo salario: {:.2f}'.format(novo_salario))
    print('Reajuste ganho: {:.2f}'.format(ganho))
    print('Em percentual: {:.0f} %'.format(reajuste))