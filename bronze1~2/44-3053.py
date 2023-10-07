import sys
input = sys.stdin.readline
N = int(input())

A=[]

for i in range(N):
    x = (int(input()))  
    A.append(x%42)

print(len(set(A)))
