N = int(input())
score = [[],[],[]]
result =[]

for i in range(N):
    a,b,c = map(int,input().split())
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)

for i in range(N):
    sum  =0
    for k in range(3):
        if score[k].count(score[k][i])==1:
            sum+=score[k][i]
    result.append(sum)

for i in result:
    print(i)