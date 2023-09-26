from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

stack = deque()

for i in range(N):
    A = input().split()

    if A[0]=='push':
        stack.append(A[1])
    elif A[0]=='pop':
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print('-1')
    elif A[0]=='size':
        print(len(stack))
    
    elif A[0] =='empty':
        if not stack:
            print('1')
        else:
            print('0')
    elif A[0] == 'top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])

    