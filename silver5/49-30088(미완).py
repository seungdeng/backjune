N = int(input())

A = []
result = []
for i in range(N):
    A = list(map(str,input().split()))
    A = int(A)
    result[i] = sum(A[1:])
    
result.sort()

hap = 0

for i in result:
    for k in i :
        hap += i

print(hap)

