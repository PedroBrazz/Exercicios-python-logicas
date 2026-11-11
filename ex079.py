vet = []

while True:
    res = int(input('Digite um valor:' ))
    if res in vet:
        print('Valor duplicado! Não vou adicionar...')
        
    else:
        vet.append(res)
    cont = str(input('Deseja continuar?[s/n]: ')).lower

    if cont == 'n':
        print(f'-=-'*50)
        print(f'Você digitou os valores {vet}')
        break

