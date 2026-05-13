media = 0
soma = 0
maior = 0
menor = 100000000
cont = 0
for c in range(1,5):
    print('-'*10, '{}ª pessoa'.format(c), '-'*10 )
    nom = str(input('Nome: '))
    ida = int(input('Idade: '))
    sex = str(input('Sexo[M/F]: ')).strip().upper()
    soma += ida
    media = soma / c
    if sex == 'M':
        if ida > maior:
            maior = ida
            nome = nom
    elif sex =='F':
        if ida < 20:
            cont += 1
print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
