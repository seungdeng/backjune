
for i in range(3):
    S = list(map(int,input().split()))
    result = S.count(0)
    if result == 4:
        print('D')
    elif result==1:
        print('A')
    elif result==2:
        print('B')
    elif result==3:
        print('C')
    elif result==0:
        print('E')