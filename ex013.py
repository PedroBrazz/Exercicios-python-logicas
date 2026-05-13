sal = float(input('Qual é o salário do funcionário? R$'))
aum = int(input('Qual a porcentagem do aumneto do salário?'))
novo = sal + (aum/100) * sal
print('Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${:.2f}'.format(sal, aum, novo))
