a,b,c,d,n = map(int,input().split())
sum = a+b+c+d
n4 = n*4

if n4-sum>0:
    print(n4-sum)
else:
    print(0)


# print(n*4-a-b-c-d) 동률의 케이스를 나눠줘야했음