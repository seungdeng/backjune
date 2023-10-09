N = int(input())
tree = {}

for i in range(1,N):
    left,right = map(str,input().split())
    tree[i] = [left,right]

