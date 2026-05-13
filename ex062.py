print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais!= 0:
    total += mais
    while cont <= total :
        print('{} -> '.format(termo), end='')
        termo += raz
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer?' ))
print('FIM ')