T = int(input())

for i in range(T):
    a,b = map(str,input().split())
    a = int(a)
    b = list(map(str,b))
    for j in range(len(b)):
        print(b[j]*a,end='')
    print('')