n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

v = (n1, n2, n3, n4)
print(f'Vôce digitou os valores {v}')
cont9 = 0
pares = []
pos = 0
for k in v:
    if k == 9:
        cont9 +=1
    if k % 2 == 0:
        pares.append(k)
for i in range(4):
    if v[i] == 3:
        pos = i + 1
        break
print(f'Vôce digitou o 9 {cont9} vezes')
print(f'O primeiro 3 foi digitado na posição {pos}')
print(f'Pares: {pares}')
