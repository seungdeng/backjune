T =int(input())
dict = {1:'Korea',2:'Yonsei',3:'Draw'}


for i in range(T):
    korea=0
    yonsei=0
    for j in range(9):
        x,y = map(int,input().split())
        yonsei+=x
        korea+=y
    if korea>yonsei:
        print('Korea')
    elif korea<yonsei:
        print('Yonsei')
    else:
        print('Draw')