N = int(input())

Que = list(map(int,input().split()))
count = 1
result = 0

for i in Que:
    if i==1:
        result+=count
        count+=1
    elif i==0:
        count=1
print(result)