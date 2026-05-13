print('='*10, 'Loja Guanabara', '='*10)
preço = float(input('preço das compras: R$'))
print('Formas de pagamneto')
print('[1] à vista em dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
op = int(input('Qusl é a opção?' ))
if op == 1 :
    valor = preço * 0.9
    print('Valor final R${:.2f}'.format(valor))
elif op == 2 :
    valor = preço * 0.95
    print('Valor final R${:.2f}'.format(valor))
elif op == 3 :
    parcela = preço / 2
    print('Valor final R${:.2f}, com parcelas de R${:.2f}'.format(preço, parcela))
else :
    parcelas = int(input('Quantas parcelas?'))
    valor = preço * 1.2
    parcela = valor / parcelas
    print('Valor final de R${:.2f}, parcelado em {}x de R${:.2f}'.format(valor, parcelas, parcela))
