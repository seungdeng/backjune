result = 0
people =0

for i in range(1,6):
    a,b,c,d = (map(int,input().split()))
    if result<(a+b+c+d):
        people=i
        result=a+b+c+d

print(people,result)
