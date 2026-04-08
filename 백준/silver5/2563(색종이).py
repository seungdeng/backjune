S = [[0 for i in range(101)]for i in range(101)]

N = int(input())

for i in range(N):
    x,y = list(map(int,input().split()))

    for j in range(x,x+10):
        for k in range(y,y+10):
            S[j][k] = 1

result = 0

for i in S:
    result+=i.count(1)

print(result)