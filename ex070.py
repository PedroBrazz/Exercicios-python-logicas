tot = 0
pmenor = 1000000000000000
cont = 0
menor = ''
print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
while True:
    nome = str(input('Nome: '))
    pre = float(input('Preço: '))
    tot = tot + pre
    conti = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pre >= 1000:
        cont += 1
    if pre < pmenor:
        menor = nome
        pmenor = pre
    if conti == 'N':
        break
print(f'{'fim do programa':-^40}')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00 um produto')
print(f'O produto mais barato foi a {menor} que custa R${pmenor:.2f} ')
