N = int(input())
A = list(map(int,input().split()))

a = max(A)

A.sort(reverse=True)
i=1
for i in range(N):
    A[i] = A[i]/a*100

result = round(sum(A)/N,5)
print(str(result))