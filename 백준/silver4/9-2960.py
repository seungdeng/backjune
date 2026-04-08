N,K = map(int,input().split())

temp = 0

S = [True]*(N+1)

for i in range(2,N+1):
    for j in range(i,N+1,i):
        if S[j] != False:
            S[j] = False
            temp+=1
            if temp==K:
                print(j)