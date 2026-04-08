import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int,input().split()))
press = sorted(set(S))

#result = {press[i]:i for i in range(len(press))}
result = {}
for i in range(len(press)):
    result[press[i]] = i    

for i in S:
    print(result[i],end=' ')    