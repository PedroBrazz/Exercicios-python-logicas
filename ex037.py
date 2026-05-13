num = int(input('Digite um número inteiro:' ))
print('Escolha uma das bases para conversão')
print('[1] Base Binária')
print('[2]Base Octal')
print('[3]Base Hexadecimal')
opc = int(input('Sua opção:'))

if opc == 1:
    print('O número {} em binário é igual a {}'.format(num, bin(num)[2:]))

elif opc == 2 :
    print('O número {} em octal é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3 :
    print('O número {} em hexadecimal é igual a {}'.format(num, hex(num)[2:]))