n = int(input())

for i in range(n):
    if n%2==1:
        a= n//2+1
        b= n//2
    else:
        a = n//2
        b = n//2

    print('* '*a)
    print(' *'*b)