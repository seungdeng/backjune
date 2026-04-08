from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

Q = deque()

for i in range(N):
    text = input().split()

    if text[0] =='1':
        Q.appendleft(text[1])
    elif text[0] =='2':
        Q.append(text[1])
    elif text[0] == '3':
        if not Q:
            print('-1')
        else:
            print(Q[0])
            Q.popleft()
    elif text[0] == '4':
        if not Q:
            print('-1')
        else:
            print(Q[-1])
            Q.pop()
    elif text[0]=='5': 
        print(len(Q))
    elif  text[0] == '6':
        if not Q:
            print('1')
        else:
            print('0')
    elif text[0] == '7':
        if not Q:
            print('-1')
        else:
            print(Q[0])
    elif text[0] == '8':
        if not Q:
            print('-1')
        else:
            print(Q[-1])   
