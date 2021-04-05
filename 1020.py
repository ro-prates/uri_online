quantidade = int(input())
anos = 0
meses = 0 
dias = 0
anos = quantidade // 365
if anos > 0:
    quantidade = quantidade - anos*365

meses = quantidade // 30
if meses > 0:
    quantidade = quantidade - meses*30

dias = quantidade

print(anos,'ano(s)')
print(meses, 'mes(es)')
print(dias, 'dia(s)')