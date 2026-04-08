N = int(input())

space = ' '
star = '*'
a = N-1
b = 1

for i in range(N):
    print(space*a,end='')
    print(star*b)
    a-=1
    b+=2