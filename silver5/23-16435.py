N,L = map(int,input().split())

a = list(map(int,input().split()))

a.sort(reverse=False)

for i in range(N):
    if L >= a[i]:
        L +=1

print(str(L))    