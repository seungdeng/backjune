N,M = map(int,input().split())

S = [0]*N

for k in range(M):
    i,j,k  = map(int,input().split())
    S[i-1:j] = [k]*(j-i+1)

print(' '.join(map(str,S)))