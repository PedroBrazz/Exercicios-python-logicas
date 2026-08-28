n = int(input('Digite um número: '))
div = []
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        div.append(c)
        cont += 1
if cont > 2:
    print('O número {} foi divisvel por {} números, sendo eles {}, com isso ele não é primo'.format(n, cont, div))
elif cont<= 2:
    print('O número {} foi divisivel apenas por 1 e ele mesmo, assim sendo primo'.format(n))



