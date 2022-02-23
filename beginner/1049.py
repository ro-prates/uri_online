primeiro = input()
segundo = input()
terceiro = input()

if primeiro == 'vertebrado':
    if segundo == 'ave':
        if terceiro == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if terceiro == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if segundo == 'inseto':
        if terceiro == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if terceiro == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')