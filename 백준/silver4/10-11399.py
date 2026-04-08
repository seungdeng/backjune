N = int(input())

A = list(map(int,input().split()))
result = 0
A.sort(reverse=0)


for i in range(1,N+1):
    result += sum(A[:i])
print(result)