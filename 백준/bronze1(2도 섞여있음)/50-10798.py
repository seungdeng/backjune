S = []

for i in range(5):
    a = input()
    S.append(a)


for k in range(15):
    for j in range(5):
        if k < len(S[j]):
            print(S[j][k],end='')