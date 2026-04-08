from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Q = deque(enumerate(map(int,input().split())))

result = []

while Q:
    idx, present = Q.popleft()
    result.append(idx+1)

    if present>0:
        Q.rotate(-(present-1))
    elif present<0:
        Q.rotate(-(present))

print(' '.join(map(str,result)))


# N = int(input())

# S = list(map(int,input().split()))
# Q = list(map(int,S))

# cal = 0
# present = 0
# for i in range(N):
#     print(S.index(Q(cal))+1,end=' ')
#     present = Q.pop(cal)
#     if present > 0 :
#         cal = present-1
#     else:
#         cal = present+1


