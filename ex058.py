from random import randint
print('Sou seu computador vou pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palp = 11
cont = 0
comp = randint(0, 10)
while palp != comp :
    cont += 1
    palp = int(input('Qual seu palpite? '))
    if palp < comp :
        print('Mais... Tente outra vez')
    elif palp > comp :
        print('Menos... Tente outra vez')
print('Acertou em {} tentaivas'.format(cont))
print(comp)