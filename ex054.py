from datetime import date
contm = 0
contma = 0
for c in range(1,8):
    n = int(input('Em que ano a {}° nasceu? '.format(c)))
    idade = date.today().year - n
    if idade < 18:
        contm += 1
    else:
        contma += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(contma))
print('E também tivemos {} pessoas menores de idade'.format(contm))

