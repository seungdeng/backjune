S = list(map(int,input().split()))

if S[0]<1:
    print(1,end=' ')
elif S[0]>1:
    print(1-S[0],end=' ')
else:
    print(0,end=' ')

if S[1]<1:
    print(1,end=' ')
elif S[1]>1:
    print(1-S[1],end=' ')
else:
    print(0,end=' ')


if S[2]<2:
    print(2-S[2],end=' ')
elif S[2]>2:
    print(2-S[2],end=' ')
else:
    print(0,end=' ')

if S[3]<2:
    print(2-S[3],end=' ')
elif S[3]>2:
    print(2-S[3],end=' ')
else:
    print(0,end=' ')

if S[4]<2:
    print(2-S[4],end=' ')
elif S[4]>2:
    print(2-S[4],end=' ')
else:
    print(0,end=' ')

if S[5]<8:
    print(8-S[5],end=' ')
elif S[5]>8:
    print(8-S[5],end=' ')
else:
    print(0)


