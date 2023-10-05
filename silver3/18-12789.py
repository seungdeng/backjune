from collections import deque
# import sys
# input = sys.stdin.readline

N = int(input())
Q = deque(map(int,input().split()))  #대기줄
wait= deque() # 빠져서 대기하는줄

result = [] #번호표대로 선 최종값

idx = 1

while Q:
    if Q[0] != idx:
        wait.append(Q.popleft())
    elif Q[0]==idx:
        result.append(Q.popleft())
        idx+=1
        

for i in range(len(wait)):
    result.append(wait.pop())

check=1
boolcheck = 1
for k in range(len(result)):
    if result[k]!=check:
        boolcheck = 0
        break
    elif result[k] == check:
        check+=1

if boolcheck == 1:
    print("Nice")
elif boolcheck ==0:
    print("Sad")