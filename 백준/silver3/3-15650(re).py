# from itertools import combinations, permutations
N,M = map(int,input().split())

A = []
def solution(q):
    if len(A)==M:
        print(' '.join(map(str,A)))
        return
    for i in range(q,N+1):
        if i not in A:
            A.append(i)
            solution(i+1)
            A.pop()

solution(1)

