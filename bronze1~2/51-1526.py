N= int(input())

while 1:
    check = True
    for i in str(N):
        if i !='4' and i != '7':
            check = False
            N-=1
    if check:
        print(N)
        break