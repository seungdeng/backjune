N,K = map(int,input().split())
coin =[]
for i in range(N):
    coin.append(int(input()))

dp =[0]*(K+1)
dp[0]=1

for i in coin:
    for k in range(i,K+1):
        if k-i >=0:
            dp[k] += dp[k-i]
print(dp[k])

# 재확인요망