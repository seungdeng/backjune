N = int(input())
P = [0]+list(map(int,input().split()))
dp = [0 for i in range(N+1)]

for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max((dp[i],dp[i-k]+P[k]))
print(max(dp))