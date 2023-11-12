N = int(input())

star = '*'
space = ' '

a =1
b = N-1

for i in range(N):
    print(space*b,end='')
    print(star*a)
    a+=1
    b-=1

a-=1
b+=1    

for i in range(N-1):
    a-=1
    b+=1  
    print(space*b,end='')
    print(star*a)  
