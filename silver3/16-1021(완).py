from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

S = list(map(int,input().split()))
Q = deque(range(1,N+1))
# for i in range(1,N+1):
#     Q.append(i)

count = 0 # 시프트시행횟수
# search = len(S)-1
for num in S:
    while True:
        if Q[0] == num:
            Q.popleft()
            break
        elif Q.index(num) > len(Q)//2:
            Q.rotate(1)
            count+=1
        else:
            Q.rotate(-1)
            count+=1

print(count)


# while S:
#     if Q[0] == S[0]:       
#         Q.popleft()
#         del S[0]
#     elif (Q.index(S[0]-1)) >= len(Q)//2:
#          #절반보다 뒤에있는경우(3번연산)-> deque 뒤로 밀기
#         count+=1
#         cal = Q[-1]
#         Q.pop()
#         Q.appendleft(cal)
#     elif (Q.index(S[0]-1)) < len(Q)//2:
#                 #2번연산(절반보다 앞에있는경우) -> deque 앞으로 당기기
#         count+=1
#         cal = Q[0]
#         Q.popleft()
#         Q.append(cal)
# print(count)