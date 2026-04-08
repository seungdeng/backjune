import math
N = int(input())
A = list(map(int,input().split()))

cal = 0
a1=0
a2 =0

for i in range(1,N):
    cal = math.gcd(A[0],A[i])
    a1 = A[0]//cal
    a2 = A[i]//cal
    print(str(a1)+'/'+str(a2))

