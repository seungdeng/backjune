N,M = map(int,input().split())

A = []

for i in range(N):
    li = list(map(int,input().split()))
    A.append(li)

S = [[0 for j in range(M+1)] for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        S[i][j] = A[i-1][j-1]+S[i][j-1]+S[i-1][j]-S[i-1][j-1]
K = int(input())

for _ in range(K):
    a,b,c,d = map(int,input().split())
    print(S[c][d]-S[c][b-1]-S[a-1][d]+S[a-1][b-1])


# S = [[0 for j in range(M)]for i in range(N)]

# for i in range(N):
#     S[i] = map(int,input().split())

# K = int(input())

# for q in range(K):
#     A = list(map(int,input().split()))
    