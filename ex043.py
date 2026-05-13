peso = float(input('Qual seu peso em Kg? '))
alt = float(input('qual sua altura em m? '))
imc = peso/(alt * alt)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Peso abaixo do ideal')
elif 18.5 < imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Peso acima do ideal')
elif 30 <= imc :
    print('Procure um médico, grau de obesidade')