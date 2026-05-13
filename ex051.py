print('='*30 )
print('10 Termos de Uma Pa ')
print('='*30 )
ter = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
soma = 0
for c in range(1,11):
    print('{}'.format(ter), end=' -> ',  )
    soma = ter + raz
    ter = soma
print('Acabou')


