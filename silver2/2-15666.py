N,M = map(int,input().split())

cal = sorted(list(set(map(int,input().split()))))
S = []

def solution(i,arr,l,num):
    if l==M:
        print(' '.join(map(str,arr)))
        return
    for j in range(i,len(num)):
        num = S[j]
        solution(j,arr+' '+num,l+1,S)
        # S.append(cal[i])
        # idx+=1
        # solution(idx,set+1)
        # S.pop()

solution(i,S[i],1,S)