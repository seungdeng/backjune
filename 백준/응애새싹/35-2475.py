S = list(map(int,input().split()))

result = 0

for i in range(len(S)):
    result += S[i]**2

print(result%10)