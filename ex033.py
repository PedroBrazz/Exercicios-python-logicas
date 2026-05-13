a = int(input('Digite um valor:'))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor: '))
menor = a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))