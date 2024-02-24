T = int(input())

for i in range(T):
    tri = list(map(int,input().split()))
    tri.sort(reverse=1)
    print('Case #'+str(i+1)+':',end=' ')
    if tri[0]==tri[1]==tri[2]:
        print('equilateral')
    elif tri[0]==tri[1] or tri[0]==tri[2] or tri[1]==tri[2]:
        print('isosceles')
    elif tri[0]*tri[0] <= tri[1]*tri[1] + tri[2]*tri[2]:
        print('scalene')
    else:
        print('invalid!')