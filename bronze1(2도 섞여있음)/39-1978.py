N = int(input())
A = map(int,input().split())

sosu = 0

for i in A:
    count = 0
    if i>1:
        for k in range(2,i):
            if i%k ==0:
                count+=1
        if count ==0:
            sosu+=1

print(sosu)