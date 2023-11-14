import sys
from collections import deque
num = int(sys.stdin.readline())

for _ in range(num):
    a,b = map(int, sys.stdin.readline().split())
    que = list(map(int, sys.stdin.readline().split()))
    ind = list(i for i in range(len(que)))
    cnt = 0
    while b in ind:
        while max(que) != que[0]:
            que.append(que.pop(0))
            ind.append(ind.pop(0))
        que.pop(0)
        ind.pop(0)
        cnt += 1
    print(cnt)



# import sys
# input = sys.stdin.readline
# T = int(input())

# for i in range(T):
#     N,M = map(int,input().split())
#     S = list(map(int,input().split()))
#     sortlist= list(i for i in range(len(S)))
    


