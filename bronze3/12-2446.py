N= int(input())

space =' '
star = '*'
a=0
b= N*2-1


for i in range(N):
    print(space*a,end='')
    print(star*b)
    a+=1
    b-=2

a-=2
b+=4
for k in range(N-1):
    print(space*a,end='')
    print(star*b)
    a-=1
    b+=2