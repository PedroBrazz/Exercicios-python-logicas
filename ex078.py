list = []

for i in range(5):
    n = int(input(f'Digite um valor para a posição {i}: '))
    list.append(n)

print('-=-'*20)
print(f'Você digitou os valores [{list[0]}, {list[1]}, {list[2]}, {list[3]}, {list[4]}]')
maior = list[0]
menor = list[0]
maiores = []
menores = []


for i in range(5):
    if list[i] > maior:
        maior = list[i]

print(f'O maior valor digitado foi {maior} nas posições', end =' ')

for j in range(5):
    if list[j] == maior:
        maiores.append(j)
for k in range(len(maiores)):
    print(f'{maiores[k]}...', end =' ')

print()

for i in range(5):
    if list[i] < menor:
        menor = list[i]
print(f'O menor valor digitado foi {menor} nas posições', end =' ')
for j in range(5):
    if list[j] == menor:
        menores.append(j)
for k in range(len(menores)):
    print(f'{menores[k]}...', end =' ')


