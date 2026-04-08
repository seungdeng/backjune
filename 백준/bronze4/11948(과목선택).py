result=0
S1 = []
S2 =[]

for i in range(4):
    S1.append(int(input()))
S1.sort(reverse=0)

S1 = S1[1:]

for i in range(2):
    S2.append(int(input()))
S2.sort(reverse=0)
S2 = S2[1:]

print(sum(S1)+sum(S2))
