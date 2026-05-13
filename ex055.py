maior = 0
menor = 100000000000000
for c in range(1,6):
    n = float(input('Peso da {}° pessoa? '.format(c)))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
print('O maior peso lido foi de {:.1f}KG'.format(maior))
print('O menor peso lido foi de {:.1f}KG'.format(menor))