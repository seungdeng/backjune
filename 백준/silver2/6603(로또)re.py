from itertools import combinations,permutations

# result=[]
# def solution(x):
#     if len(result)==6:
#         print(' '.join(map(str,result)))
#         return
#     for i in range(len(S)):
#         if S[i] not in result:
#             result.append(S[i])
#             solution(i+1)
#             result.pop()
while 1:
    S = list(map(int,input().split()))
    stop = S[0]
    num = S[1:]
    if stop==0:
        exit()
    
    for i in combinations(num,6):
        print(*i)
    print()


# def dfs(depth, idx):
#     if depth == 6:
#         print(*out)
#         return

#     for i in range(idx, k):
#         out.append(S[i])
#         dfs(depth + 1, i + 1)
#         out.pop()


# while True:
#     array = list(map(int, input().split()))
#     k = array[0]
#     S = array[1:]
#     out = []
#     dfs(0, 0)
#     if k == 0:
#         exit()
#     print()    