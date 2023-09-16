
while True:
    num = list(map(int,input().split()))
    if sum(num) ==0:
        break;
    
    highnum = max(num)
    num.remove(highnum)
    
    if num[0]**2+num[1]**2==highnum**2:
        print("right")
    else:
        print("wrong")