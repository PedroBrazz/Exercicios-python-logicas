dias =  int(input('Quantos dias alugados?'))
km = float(input('Quantos Kms rodados?'))
valor = dias * 60 + 0.15 * km
print('O total a pagar é de R${:.2f}'.format(valor))