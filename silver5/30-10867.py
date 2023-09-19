N = input()

S = list((map(int,input().split())))
S = list(set(S))
S.sort()

for i in S:
    print(i,end= " ")
