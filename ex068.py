from random import randint
print('=-'* 30)
print('Vamos jogar par ou ímpar')
print('=-'* 30)
while True:
    ter = int(input('Diga um valor: '))
    esc = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print('-'*30)
    comp = randint(1,10)
    soma = ter + comp
    res = (comp + ter) % 2
    print(f'Você jogou {ter} e o computador {comp}. Total de {soma}')
    if esc == 'P':
        if res == 0:
            print('Você Venceu')
            print('Vamos jogar novamente')
            print('=-'* 30)
        else:
            print('Você perdeu')
            break
    elif esc == 'I':
        if res ==1:
            print('Você Venceu')
            print('Vamos jogar novamente')
            print('=-'* 30)
        else:
           print('Você perdeu')
           break
print('GAME OVER')