from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

Q = deque()

for i in range(N):
    data = input().split()

    if data[0] == 'push_front':
        Q.appendleft(data[1])
    elif data[0] == 'push_back':
        Q.append(data[1])
    elif data[0] == 'pop_front':
        if not Q:
            print('-1')
        else:
            print(Q[0])
            Q.popleft()
    elif data[0] == 'pop_back':
        if not Q:
            print('-1')
        else :
            print(Q[-1])
            Q.pop()
    elif data[0] =='size':
        print(len(Q))
    elif data[0] =='empty':
        if not Q:
            print('1')
        else:
            print('0')
    elif data[0] =='front':
        if not Q:
            print('-1')
        else:
            print(Q[0])
    elif data[0] =='back':
        if not Q:
            print('-1')
        else:
            print(Q[-1])
        
    
        