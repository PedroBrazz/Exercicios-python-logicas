from random import randint
computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar')
print('-=-'*20)
num = int(input('Em que número pensei? '))
if num == computador:
    print('Parabéns! Você conseguiu vencer!')
else :
    print('Ganhei! Eu pensei no numero {} e não no {}'.format(computador, num))
