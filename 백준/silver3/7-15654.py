# import sys
# sys.setrecursionlimit(10**8)
# input = sys.stdin.readline

# N,M = map(int,input().split())

# S =list(map(int,input().split()))
# S.sort(reverse=0)
# result = []

# def dfs():
#     if len(result)==M:
#         print(' '.join(map(str,result)))
#         return
    
#     for i in range(0,N):
#         result.append(S[i])
#         dfs()
#         result.pop()

# dfs()

N,M = map(int,input().split())

S =list(map(int,input().split()))
S.sort(reverse=0)
visit = [False]*N
result=[]
def dfs(K,N,M):
    if K==M:
        print(' '.join(map(str,result)))
        return
    
    for i in range(N):
        if not visit[i]:
            visit[i] =True
            result.append(S[i])
            dfs(K+1,N,M)
            result.pop()
            visit[i]=False

dfs(0,N,M)