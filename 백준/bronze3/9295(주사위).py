N = int(input())

for i in range(N):
    x,y = map(int,input().split())
    print('Case',i+1,end='')
    print(': ',end='')
    print(x+y)