sal = float(input('Qual o salário do funcionário? R$'))
saln = 0
if sal >= 1250:
    saln = sal *1.1
if sal <= 1250:
    saln = sal * 1.15

print('Quem ganhava R${:.2f} passará a ganhar R${:.2f}'.format(sal, saln))