N = int(input())
rope = []

for i in range(N):
    rope.append(int(input()))

rope.sort(reverse=1)
result = []

for j in range(N):
    result.append(rope[j]*(j+1))
print(max(result))