res = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while res == 'S':
    num = (int(input('Digite um número: ')))
    res = (str(input('Quer continuar? [S/N] '))).strip().upper()[0]
    cont += 1
    soma = soma + num
    med = soma /cont
    if num >= maior:
        maior = num
    if menor >= num:
        menor = num
print(f'Você digitou {cont} números e a média foi de {med:.2f}')
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
