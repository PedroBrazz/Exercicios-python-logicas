pre = float(input('Qual o preço do produto? R$'))
des = int(input('Qual a porcentagem do desconto?'))
print('O produto que antes custava {}, na promção de {}% vai custar R${:.2f}'.format(des, pre, pre * 0.95))