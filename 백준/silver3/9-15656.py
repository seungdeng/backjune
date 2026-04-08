N,M = map(int,input().split())

A = list(map(int,input().split()))

A.sort(reverse=0)

result = []

def solution():
    if len(result)==M:
        print(' '.join(map(str,result)))
        return
    
    for i in range(N):
        result.append(A[i])
        solution()
        result.pop()


solution()

