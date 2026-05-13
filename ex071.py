cont50 = cont20 = cont10 = cont5 = cont1 = 0

print(f'{"Banco CEV":=^40}')
val = int(input('Que valor você quer sacar? R$ '))

# Usaremos o próprio 'val' para ir diminuindo o saldo
while True:
    while val >= 50:
        val -= 50
        cont50 += 1

    while val >= 20:
        val -= 20
        cont20 += 1

    while val >= 10:
        val -= 10
        cont10 += 1

    while val >= 5:
        val -= 5
        cont5 += 1

    while val >= 1:
        val -= 1
        cont1 += 1

    # Quando o valor chegar a zero, o saque terminou
    if val == 0:
        break

print(f'Total de {cont50} cédulas de R$50')
print(f'Total de {cont20} cédulas de R$20')
print(f'Total de {cont10} cédulas de R$10')
print(f'Total de {cont5} cédulas de R$5')
print(f'Total de {cont1} cédulas de R$1')

