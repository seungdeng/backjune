from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Q = deque()

for i in range(N):
    data = input().split()
    if data[0] == '1':
        Q.append(data[1])
    elif data[0] == '2':
        if not Q:
            print('-1')
        else :
            print(Q[-1])
            Q.pop()
    elif data[0] == '3':
        print(len(Q))
    elif data[0] == '4':
        if not Q:
            print('1')
        else:
            print('0')
    elif data[0] == '5':
        if not Q:
            print('-1')
        else:
            print(Q[-1])


