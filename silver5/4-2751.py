import sys

N = int(input())
A=[]

for i in range (N):
    A.append(int(sys.stdin.readline()))

A.sort(reverse=False)

for i in range(len(A)):
    print(A[i])