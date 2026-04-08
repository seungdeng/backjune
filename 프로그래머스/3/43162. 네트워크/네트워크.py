from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(graph, start, visited):
        q = deque([start])
        visited[start] = True
        
        while q:
            v = q.popleft()
            for i in range(n):
                if graph[v][i] == 1 and not visited[i]:
                    q.append(i)
                    visited[i] = True
    for i in range(n):
        if not visited[i]:
            bfs(computers, i, visited)
            answer +=1
            
    return answer
    
    
    return answer