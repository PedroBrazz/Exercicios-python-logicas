sex = str(input('Informe seu sexo: [M/f]: ')).upper().strip()
while (sex != 'M' and sex !='F') :
    sex = str(input('DAdos inválidos. Por favor, informe seu sexo: [M/f]: ')).upper().strip()
print('Sexo {} salvo com sucesso'.format(sex))


