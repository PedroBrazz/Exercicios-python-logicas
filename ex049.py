n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    tab = n * c
    print('{} X {} = {}'.format(n, c, tab))