X = int(input())
N = int(input())

check = 0
for i in range(N):
    a,b = map(int,input().split())
    check += a*b

if X==check:
    print('Yes')
else:
    print('No')