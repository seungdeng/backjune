N = int(input())
plus = []

for i in range(N):
    plus.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(len(plus[i])):
        if  j==0:
            plus[i][j] = plus[i][j]+plus[i-1][j]
        elif j==len(plus[i])-1:
            plus[i][j] = plus[i][j]+plus[i-1][j-1]
        else:
            plus[i][j] = plus[i][j]+max(plus[i-1][j-1],plus[i-1][j])
print(max(plus[N-1]))