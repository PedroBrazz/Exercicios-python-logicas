print('-=-' *20)
print('Analisador de triângulos')
print('-=-' * 20)
ps = float(input('Primeiro segmento: '))
ss = float(input('Segundo segmento: '))
ts = float(input('Terceiro segmento: '))
if ps + ss > ts and ps + ts > ss and ss +ts>ps:
    print('Esses segmentos formam um triângulo ')
else:
    print('Esses segmentos não formam um triângulo')
