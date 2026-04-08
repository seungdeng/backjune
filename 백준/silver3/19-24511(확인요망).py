import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

style = list(map(int,input().split()))
num = list(map(int,input().split()))
M = int(input())
insert = list(map(int,input().split()))

Q = deque()

for i in range(N):
    if style[i]==0:
        Q.append(num[i])
else:
    if len(num) == 0:
        print(*insert)
        sys.exit()

for i in range(M):
    Q.appendleft(insert[i])

    print(Q.pop(),end =' ')
# for i in range(N):
#     if style[i]==0:
#         Q.appendleft(num[i])
# for k in range(M):
#     Q.append(insert[k])
#     print(Q.popleft,end=' ')

# for i in range(M): # input받은 M회만큼 진행
#     num2 = num
#     for k in range(N): #input받은 수열의 개수만큼 진행  
#         if style[k] == 0:
#             cal = num2.pop(0)
#         else:
#             num2.pop(0)
#     result.append(cal)

# print(' '.join,result)
    