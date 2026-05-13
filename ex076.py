listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Caneta', 22.3,
            'Livro', 34.9,)
print('-'*40, 'Lista', '-'*40)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<30} R${listagem[c+1]:>8.2f}')
