import random
v = []
for  i in range(5):
    v.append(random.randint(1, 10))
print(f'Os valores sorteados foram:', end=' ')
for j in range(5):
    print(v[j], end=' ')
print()
maior = 0
menor = 11
for k in v:
    if k > maior:
        maior = k
    if k < menor:
        menor = k


print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')