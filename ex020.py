from random import shuffle
nom1 = str(input('Primeiro aluno: '))
nom2 = str(input('Segundo aluno: '))
nom3 = str(input('Terceiro aluno: '))
nom4  = str(input('Quarto aluno: '))
lista = [nom1, nom2, nom3, nom4]
shuffle(lista)
print('A ordem de apresentação será \n{}'.format(lista))