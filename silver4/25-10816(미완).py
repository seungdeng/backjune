import sys
input = sys.stdin.readline

N  = int(input())
 
S = list(map(int,input().split()))

M = int(input())

result = [0]*M

Y = list(map(int,input().split()))

for i in range(N):
    if S[i] in Y:
        k = Y.index(S[i])
        result[k]+=1

print(' '.join(map(str,result)))