n1, n2, n3, n4 = input().split(" ")

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (2*n1 + 3*n2 + 4*n3 + 1*n4) / (2+3+4+1)

if media >= 7:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
else:
    exame = input()
    exame = float(exame)
    nova_media = (media + exame) / 2
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    print('Nota do exame: {:.1f}'.format(exame))
    if nova_media >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(nova_media))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(nova_media))