L,P = map(int,input().split())
people = L*P

S = list(map(int,input().split()))

for i in S:
    print(i-people,end=' ')