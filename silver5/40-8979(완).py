import sys
input = sys.stdin.readline

N,K = map(int,input().split())

medal = [list(map(int,input().split())) for i in range(N)]

medal.sort(key=lambda x:(x[1],x[2,x[3]]),reverse=True)

a = [medal[i][0] for i in range(N)].index(K)


for k in range(N):
    if medal[a][1:] == medal[k][1:]:
        print(k+1)
        break
# li =[]

# for i in range(N):
#     nation,gold,silver,bronze= map(int,input().split())
#     li.append(gold,silver,bronze,nation)

# li[:N] = sorted(li[:N],reverse=True)
    
