N,K = map(int,input().split())
result=0
count=0


for i in range(1,N+1,1):
    if N%i ==0:
        result=i
        count+=1
    if count==K:
        print(result)
        break

if count!=K:
    print(0)