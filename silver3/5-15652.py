N,M= map(int,input().split())

S =[]

def dfs(x):
    if len(S) ==M:
        print(' '.join(map(str,S)))
        return
    for i in range(x,N+1):
        S.append(i)
        dfs(i)
        S.pop()

dfs(1)