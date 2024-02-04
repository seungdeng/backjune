a,b = map(int,input().split())

result = 0

if a==b:
    print(a+b-1)
elif a>b:
    print(b+b+1)
elif a<b:
    print(a+a+1)