import random
m = [[0] * 6 for _ in range(6)]
for i in range(6):
    for j in range(6):
        num = random.randint(0,1)
        m[i][j] = num
for i in range(6):
    for j in range(6):
        print(m[i][j],end='  ')
    print()
print()
m2 = [[0] * 6 for _ in range(6)]
for i in range(6):
    for j in range(6):
        soma = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                if k == 0 and l == 0:
                    continue
                elif 0 <=i + k <6 and 0 <=j + l <6:
                    soma +=  m[i+ k][j+ l]
        if m[i][j] == 0:
            if soma == 3:
                m2[i][j] =1
        elif m[i][j] == 1:
            if soma < 2:
                m2[i][j] =0
            elif soma <= 3:
                m2[i][j] =1
            elif soma <= 4:
                m2[i][j] =0


for i in range(6):
    for j in range(6):
        if m[i][j] == 1:
            m[i][j] ='.'
        else:
            m[i][j] = 'x'
for i in range(6):
    for j in range(6):
        print(m[i][j],end='  ')
    print()

print()
for i in range(6):
    for j in range(6):
        if m2[i][j] == 1:
            m2[i][j] ='.'
        else:
            m2[i][j] = 'x'
for i in range(6):
    for j in range(6):
        print(m2[i][j],end='  ')
    print()



