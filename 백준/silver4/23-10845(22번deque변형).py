from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

Q = deque()


for i in range(N):
    cal= input().split()

    if cal[0]=='push':
        Q.append(cal[1])
       # print(cal[1])
    elif cal[0] =='pop':
        if not Q:
            print('-1')
        else:
            print(Q[0])
            Q.popleft()
    elif cal[0]=='size':
        print(len(Q))
    elif cal[0]=='empty':
        if Q:
            print('0')
        else:
            print('1')
    elif cal[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print('-1')
    elif cal[0] =='back':
        if Q:
            print(Q[-1])
        else:
            print('-1')

        
