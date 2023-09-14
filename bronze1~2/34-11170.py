T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    count = 0
    for i in range(N,M+1,1):
        for A in str(i):
            if A=="0":
                count+=1
    
    print(count)