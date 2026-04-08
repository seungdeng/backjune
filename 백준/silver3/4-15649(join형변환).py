from itertools import combinations, permutations
N,M = map(int,input().split())

num = list(range(1,N+1,1))
num = ''.join(map(str,num)) 

combi = (list(map(' '.join,permutations(num,M))))

for i in combi:
    print(i)



# join은 문자열만 가능