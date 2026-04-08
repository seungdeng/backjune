from collections import deque

N,K = map(int,input().split())
Q = deque()
result =[]
for i in range(1,N+1):
    Q.append(i)

while Q:
    for i in range(K-1):
        num=Q.popleft()
        Q.append(num)
    result.append(Q.popleft())

print('<',end='')
for i in range(len(result)-1):
    print(result[i],end='')
    print(', ',end='')
print(result[-1],end='')
print('>')

    