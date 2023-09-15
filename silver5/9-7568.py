N = int(input())

A = []

for i in range(N):
    [a,b] = map(int,input().split())
    A.append([a,b])

for i in A:
    rank= 1
    for k in A:
        if i[0]<k[0] and i[1] <k[1]:
            rank+=1
    
    print(rank,end=" ")