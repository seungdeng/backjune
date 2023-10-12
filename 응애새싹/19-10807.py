N = int(input())
S = list(map(int,input().split()))
v = int(input())

cnt = 0
for i in range(len(S)):
    if v == S[i]:
        cnt+=1
print(cnt)