T = int(input())

for i in range(T):
    price= 0
    car = int(input())
    price+=car
    option = int(input())
    if option!=0:
        for i in range(option):
            q,p = map(int,input().split())
            price+=(q*p)
    print(price)