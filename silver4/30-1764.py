N,M = map(int,input().split())

S = set()
result = []

for i in range(N):
    S.add(input())

for k in range(M):
    word = input()
    if word in S:
        result.append(word)
result.sort(reverse=False)

print(len(result))
for j in result:
    print(j)
