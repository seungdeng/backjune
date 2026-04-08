from collections import deque
N = int(input())
M = int(input())

graph = [[] for i in range(N+1)]
visit = [0]*(N+1)

for i in range(M):
    a,b = map(int,input().split())
    graph[a] +=[b]
    graph[b] +=[a]

# visit[1] = 1

# # Q = deque([1])

# while Q:  #BFS 너비우선
#     C = Q.popleft()
#     for k in graph[C]:
#         if visit[k] ==0:
#             Q.append[k]
#             visit[k]=1

# print(sum(visit)-1)

#DFS 깊이우선

def dfs(q):
    visit[q] = 1
    for i in graph[q]:
        if visit[i]==0:
            dfs(i)
dfs(1)
print(sum(visit)-1)