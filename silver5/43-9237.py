N = int(input())


A =list(map(int,input().split()))

A.sort(reverse=True)

result = []

for i in range(N):
    result.append(A[i]+1+i)

print(max(result)+1)