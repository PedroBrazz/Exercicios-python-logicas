seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))
if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    if seg1 == seg2 == seg3:
        print('O triângulo é possível e é equilátero')
    elif seg1 == seg2 and (seg1 > seg3 or seg1 < seg3):
        print('O triângulo é possível e é isósceles')
    elif seg1 == seg3 and (seg1 > seg2 or seg1 < seg2):
        print('O triângulo é possível e é isósceles')
    elif seg2 == seg3 and (seg2 > seg1 or seg2 < seg1):
        print('O triângulo é possível e é isósceles')
    elif seg3 == seg1 and (seg3 > seg2 or seg3 < seg2):
        print('O triângulo é possível e é isósceles')
    else:
        print('O triângulo é possível e é escaleno')
else:
    print('O triângulo é impossível')
