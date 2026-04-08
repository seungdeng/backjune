from collections import deque
import sys
input = sys.stdin.readline

Q = deque()

angle = 0
N = int(input())

for i in range(N):
    data = input().split()
    if data[0] == 'push':
        Q.append(data[1])
    elif data[0] == 'pop':
        if Q:
            Q.pop()
    elif data[0]== 'rotate':
        if data[1]=='1':
            angle+=90
        elif data[1]=='r':
            angle-=90
