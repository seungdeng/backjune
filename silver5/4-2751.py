N = int(input())
A=[]

for i in range (N):
    A.append(int(input()))

A.sort(reverse=False)

for i in range(len(A)):
    print(A[i])