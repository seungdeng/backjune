from collections import deque
import sys
input = sys.stdin.readline

Q = deque()

N = int(input())

for i in range(N):
    data = input().split()

    if data[0] == 'push':
        Q.append(data[1])
    elif data[0] == 'pop':
        if not Q:
            print('-1')
        else:
            print(Q[0])
            Q.popleft()
    elif data[0]=='size':
        print(len(Q))
    elif data[0] == 'empty':
        if not Q:
            print('1')
        else:
            print('0')
    elif data[0]=='front':
        if not Q:
            print('-1')
        else:
            print(Q[0])
    elif data[0] == 'back':
        if not Q:
            print('-1')
        else:
            print(Q[-1])

    