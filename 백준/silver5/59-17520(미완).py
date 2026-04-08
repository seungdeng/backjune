from itertools import combinations, permutations

N = int(input())

A = [x for x in range(N)]

result = list(combinations(A,2))

print(result)
