print('-'*20)
print('Sequencia de Fibonacci')
print('-'*20)
num = int(input('Quantos termos deseja mostrar: '))
print('-'*20)
t1 = 0
t2 = 1
cont = 3
while cont <= num:
    t3 = t1 + t2
    print('{}'.format(t3),end = ' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
