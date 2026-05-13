from random import randint
print('Suas opções')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] Tesoura')
jog = int(input('Qual sua jogada?' ))
print('JO')
print('KEN')
print('PO')
print('-=' * 12)
cpu = randint(0,2)
if jog == 0 :
    if cpu == 0:
        print('Computador jogou Pedra')
        print('Jogador jogou Pedra ')
        print('-=' * 12)
        print('Empate')
    if cpu == 1:
        print('Computador jogou Papel')
        print('Jogador jogou Pedra')
        print('-=' * 12)
        print('Computador ganhou')
    if cpu == 2:
        print('Computador jogou Tesoura')
        print('Jogador jogou Pedra ')
        print('-=' * 12)
        print('Jogador Ganhou')
if jog == 1:
    if cpu == 0:
        print('Computador jogou Pedra')
        print('Jogador jogou Papel')
        print('-=' * 12)
        print('Jogador ganhou')
    if cpu == 1:
        print('Computador jogou Papel')
        print('Jogador jogou Papel ')
        print('-=' * 12)
        print('Empate')
    if cpu == 2:
        print('Computador jogou Tesoura')
        print('Jogador jogou Papel ')
        print('-=' * 12)
        print('Computador ganhou')
if jog == 2 :
    if cpu == 0:
        print('Computador jogou Pedra')
        print('Jogador jogou Tesoura')
        print('-=' * 12)
        print('Computador ganhou')
    if cpu == 1:
        print('Computador jogou Papel')
        print('Jogador jogou Tesoura ')
        print('-=' * 12)
        print('Jogador ganhou')
    if cpu == 2:
        print('Computador jogou Tesoura')
        print('Jogador jogou Tesoura ')
        print('-=' * 12)
        print('Empate')


