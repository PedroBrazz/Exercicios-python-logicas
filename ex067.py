while True:
    cont = 0
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if num >= 0 :
        while cont <= 9:
            cont += 1
            print(f'{num} X {cont} = {num * cont}')

    else:
        break
    print('-' * 30)
print('FIM DO PROGRAMA')