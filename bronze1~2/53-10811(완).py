N,M = map(int,input().split())

S = [k for k in range(1,N+1)]

for x in range(M) :
    i, j = map(int, input().split())
    S[i-1:j] = S[i-1:j][::-1]
    
for i in S:
    print(i,end=' ')
# print(*S)a
# for i in range(M):
#     i,j = map(int,input().split())
#     i-=1
#     S = [i:j::-1]
# print(S)