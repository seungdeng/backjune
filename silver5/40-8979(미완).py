N,K = map(int,input().split())
li =[]

for i in range(N):
    nation,gold,silver,bronze= map(int,input().split())
    li.append(gold,silver,bronze,nation)

li[:N] = sorted(li[:N],reverse=True)
    
