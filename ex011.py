larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
lm = float(input('Quantos litros de tinta pintam um m²?'))
dim = larg * alt
tin = dim / lm

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, dim))
print('Para pintar essa parede,  você precisará de {}l de tinta.'.format(tin))