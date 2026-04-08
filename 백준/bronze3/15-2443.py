N = int(input())
star = '*'
space = ' '
a=0
b= 2*N-1

for i in range(N):
    print(space*a,end='')
    print(star*b)
    a+=1
    b-=2