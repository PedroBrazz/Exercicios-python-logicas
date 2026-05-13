vel = float(input('Qual a velocidade atual do carro? '))
multa = (vel - 80) *7
if vel <= 80:
    print('Velocidade permitida')
else :
    print('Velocidade acima do limite de 80 km/h, sua multa tem o valor de R${:.2f}'.format(multa))