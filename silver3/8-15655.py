from itertools import combinations, permutations
N,M = map(int,input().split())

S = sorted(list(map(int,input().split())))
result =[]

def solution(idx,count):
    if count==M:
        print(*result)
        return
    for i in range(idx,N):
        idx+=1
        result.append(S[i])
        solution(idx,count+1)
        result.pop()

solution(0,0)


# S = list(map(int,input().split()))
# S.sort(reverse=False)
# S = ''.join(map(str,S)) 

# combi = (set(map(' '.join,permutations(S,M))))

# combi = list(combi)
# combi = sorted(combi,reverse=False)
# for i in combi:
#     print(i)



# while True:
#     if S[-1] >8:
#         S.pop()
#         N-=1
#     else:
#         break
# result = []
# visit = [False]*N

# def solution(K,N,M):
#     if K==M: # len(result)
#         print(' '.join(map(str,result)))
#         return
    
#     for i in range(N):
#         if not visit[i]:
#             visit[i] =True
#             result.append(S[i])
#             solution(K+1,N,M)
#             result.pop()
#             visit[i]=False


# solution(0,N,M)