d = float(input('Uma distância em metros:'))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d  * 10
cm  = d * 100
mm = d * 1000
print('A medida de {:.1f}m corresponde a \n{:.3f}Km \n{:.2f}Hm \n{:.1f}Dam \n{}Dm \n{}Cm \n{}Mm'.format(d, km, hm, dam, dm, cm, mm))