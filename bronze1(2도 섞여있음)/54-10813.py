N,M = map(int,input().split())

S = [i for i in range(1,N+1)]

x =0
for i in range(M):
    i,j = map(int,input().split())
    x = S[i-1]
    S[i-1] = S[j-1]
    S[j-1] = x

    # S[i-1:j]=S[i-1:j][::-1]

print(' '.join(map(str,S)))