a,b = map(int,input().split())

x=0
y=0

x = a//2

if a==1: # 빵이 한개면? 햄버거 못만들어용~
    print('0')
else:
    print(min(x,b))