from math import sqrt
cp = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = sqrt(cp**2 + ca**2)
print('A hipotenusa vai medir {:.2f}'.format(hip))