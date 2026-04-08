N,M = map(int,input().split())

cal = sorted(list(map(int,input().split())))
S = []

def solution(x):
    if len(S)==M:
        print(' '.join(map(str,S)))
        return
    for i in range(x,N):
        S.append(cal[i])
        solution(i)
        S.pop()

solution(0)