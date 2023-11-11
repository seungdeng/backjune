T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    x = 0
    for k in range(b):
        x = a**b
        x = x%10
    print(x)