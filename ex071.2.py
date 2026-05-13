val = int(input('Que valor você quer sacar? R$ '))
qnt50 = val // 50
resto = val % 50
qnt20 = resto // 20
resto = resto % 20
qnt10 = resto // 10
resto = resto % 10
qnt5 = resto // 5
resto = resto % 5
qnt1 = resto // 1
resto = resto % 1
print(f'Total de {qnt50} cédulas de R$50')
print(f'Total de {qnt20} cédulas de R$20')
print(f'Total de {qnt10} cédulas de R$10')
print(f'Total de {qnt5} cédulas de R$5')
print(f'Total de {qnt1} cédulas de R$1')

