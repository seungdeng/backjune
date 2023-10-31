S=[]
for i in range(9):
    S.append(list(map(int,input().split())))

x=0
y=0
MAX=-1

for i in range(9):
    for k in range(9):
        if S[i][k] >MAX:
            MAX = S[i][k]
            x = i+1
            y = k+1
print(MAX)
print(x,y)
