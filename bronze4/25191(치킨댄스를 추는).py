N = int(input())
ims = 0
A,B= map(int,input().split())

ims+= (A//2)
ims+=B

if N>=ims:
    print(ims)
else:
    print(N)