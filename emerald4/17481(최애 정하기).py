N,M = map(int,input().split())
name = []

for i in range(M):
    name.append(input())

for k in range(N):
    person = input().split()

visited = [False for i in range(N)]