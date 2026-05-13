casa = float(input('Qual o valor da casa: R$'))
sal = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
pres = casa / (anos * 12)
print('Para Pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, pres))
if pres <= sal *0.3:
    print('Empréstimo Aceito!')
else :
    print('Empréstimo Negado!')
