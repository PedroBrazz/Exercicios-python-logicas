enc = int(input())
n1 = enc // 1000
n2 = (enc % 1000) // 100
n3 = (enc % 100) // 10
n4 =( enc % 10)

d1 = (n1 + 1) % 10
d2 = (n2 + 1) % 10
d3 = (n3 + 1) % 10
d4 = (n4 + 1) % 10

print(f'{d1}{d2}{d3}{d4}')
