N = int(input())

space = N-1
for i in range(1,N+1):
    print(' '*space,end='')
    print('*'*i)
    space-=1