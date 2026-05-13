max = int(input())
qnt500 = max // 500
resto = max % 500
qnt100 = resto // 100
resto = resto % 100
qnt25 = resto // 25
resto = resto % 25
qnt1 = resto // 1
resto = resto % 1
print(qnt500)
print(qnt100)
print(qnt25)
print(qnt1)