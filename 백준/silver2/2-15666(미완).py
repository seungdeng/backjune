import sys
input= sys.stdin.readline

N,M = map(int,input().split())

cal = sorted(list(set(map(int,input().split()))))
S = []

def sol(start):
    if len(S) == M:
        print(' '.join,map(int,S))
        return
    x= 0
    for i in range(start,N):
        if x != cal[i]:
            S.append(cal[i])
            x = cal[i]
            sol(i)
            S.pop()
sol(0)

# def solution(i,arr,l,num):
#     if l==M:
#         print(' '.join(map(str,arr)))
#         return
#     for j in range(i,len(num)):
#         num = S[j]
#         solution(j,arr+' '+num,l+1,S)
#         # S.append(cal[i])
#         # idx+=1
#         # solution(idx,set+1)
#         # S.pop()

# solution(i,S[i],1,S)