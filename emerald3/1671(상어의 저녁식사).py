def DFS(shark):
    if visited[shark]:
        return False
    visited[shark] = True

    for i in 