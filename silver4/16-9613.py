from itertools import combinations, permutations
import math
T = int(input())



for i in range(T):
    A = list(map(int,input().split()))
    result = 0
    for j in range(1,len(A)):
        for k in range(j+1,len(A)):
            result+=math.gcd(A[j],A[k])
    print(result)




    # A.pop(0)
    # combi = list(combinations(A, 2))
    # for k in range(len(combi)):
    #     result += math.gcd(int(combi[k]))
    # print(result)