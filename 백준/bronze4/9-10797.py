date = int(input())
count =0
car = list(map(int,input().split()))

for k in car:
    if k%10 ==date:
        count+=1
print(count)