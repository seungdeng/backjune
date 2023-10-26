N,C = map(int,input().split())
S = list(map(int,input().split()))
count = dict()
idx= 1

for i in S:
    if i in count:
        count[i][0] +=1
    else:
        count[i] = [1,idx]
        idx+=1

num = [[i,j] for i,j in count.items()]
num.sort(key=lambda x:(-x[1][0],x[1][1]))
result = []

for i,j in num:
    result +=  [i]*j[0]

print(*result)