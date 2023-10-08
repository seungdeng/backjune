N = int(input())


for i in range(N):
    result = []
    A = list(map(str,input().split()))
    for k in range(len(A)):
        word = A[k]
        result.append(word[::-1])
    print(' '.join(result))