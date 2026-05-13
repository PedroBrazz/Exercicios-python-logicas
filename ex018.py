from math import cos, sin, tan, radians
ang = float(input('Digite um ângulo que você deseja: '))
print('O ângulo de {} tem o seno de {:.2f} \nO ângulo de {} tem o cosseno de {:.2f} \nO ângulo de {} tem a tangente de {:.2f}'.format(ang , sin(radians(ang)), ang, cos(radians(ang)), ang, tan(radians(ang))))

