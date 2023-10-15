import sys
input = sys.stdin.readline
N,M = map(int,input().split())

D = {}

for i in range(1,N+1):
    A = input().rstrip()
    D[i]= A
    D[A]= i

for i in range(M):
    Q = input().rstrip()
    if Q.isdigit():
        print(D[int(Q)])
    else:
        print(D[Q])