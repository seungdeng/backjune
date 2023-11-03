# from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
move = []
count = 1

line = list(map(int,input().split()))
while line:
    if count == line[0]:
        count+=1
        line.pop(0)
    else:
        move.append(line.pop(0))
    while move:
        if move[-1] == count:
            move.pop()
            count+=1
        else:
            break

if len(move) ==0:
    print("Nice")
else:
    print("Sad")
# N = int(input())
# Q = deque(map(int,input().split()))  #대기줄
# wait= deque() # 빠져서 대기하는줄

# result = [] #번호표대로 선 최종값

# idx = 1

# while Q or wait:
#     if Q and Q[0] != idx:
#         wait.append(Q.popleft())
#     elif wait and wait[-1] == idx:
#         result.append(wait.pop())
#         idx+=1
#     elif Q and Q[0]==idx:
#         result.append(Q.popleft())
#         idx+=1
        
# # for i in range(len(wait)):
# #     result.append(wait.pop())

# check=1
# boolcheck = 1
# for k in range(len(result)):
#     if result[k]!=check:
#         boolcheck = 0
#         break
#     elif result[k] == check:
#         check+=1

# if boolcheck == 1:
#     print("Nice")
# elif boolcheck ==0:
#     print("Sad")