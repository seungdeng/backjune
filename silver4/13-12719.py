import sys
input = sys.stdin.readline
N,M = map(int,input().split())

name =['0']*N
id = ['0']*N

search = ['0']*M

for i in range(N):
    name[i],id[i] = map(str,input().split())

for j in range(M):
    search[j] =input()

for k in range(M):
    print(name[(id.index(search[k]))])

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# add = {}

# for _ in range(N):
#     site, ps = input().split()
#     add[site] = ps

# for _ in range(M):
#     print(add[input().rstrip()]) 