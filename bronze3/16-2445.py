N = int(input())
star='*'
space = ' '
a=1
b=2*N-2

for i in range(N):
    print(star*a,end='')
    print(space*b,end='')
    print(star*a)
    a+=1
    b-=2
a-=1
b+=2
for k in range(N-1):
    a-=1
    b+=2

    print(star*a,end='')
    print(space*b,end='')
    print(star*a)
