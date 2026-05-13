contmais = conth = contf = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'HF':
        sexo = str(input('Sexo: [H/F] ')).strip().upper()[0]
    if idade > 18:
        contmais += 1
    if sexo == 'H':
        conth += 1
    if sexo == 'F' and idade < 20:
        contf += 1
    print('-' * 30)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {contmais}')
print(f'Ao todo temos {conth} homens cadastrados')
print(f'E temos {contf} mulheres com menos de 20 anos')
