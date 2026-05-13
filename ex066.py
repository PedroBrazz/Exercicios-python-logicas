cont = 0
soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        cont +=1
    elif num == 999:
        break
print(f'A soma dos {cont} valores foi {soma}')