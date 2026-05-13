import random
nom1 = str(input('Primeiro aluno: '))
nom2 = str(input('Segundo aluno: '))
nom3 = str(input('Terceiro aluno: '))
nom4 = str(input('Quarto aluno: '))
lista = [nom1, nom2, nom3, nom4]
print('O aluno escolhido foi {}'.format(random.choice(lista)))

