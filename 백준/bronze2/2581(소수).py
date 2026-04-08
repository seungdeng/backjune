M = int(input())
N = int(input())

numlist =[]

for i in range(M,N+1):
    countnum=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                countnum+=1
                break
        if countnum==0:
            numlist.append(i)

if len(numlist)<1:
    print(-1)
else:
    print(sum(numlist))
    print(min(numlist))