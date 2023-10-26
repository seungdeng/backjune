N = int(input())
S =[]
for i in range(N):
    S.append(input().split())

S.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in S:
    print(str(i[0]))
