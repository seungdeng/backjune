
for i in range(int(input)):
    a,b=map(int,input().split())
    result =0

    if a==1:
        result+=5000000
    elif a>=2 and a<=3:
        result+=3000000
    elif a>=4 and a<=6:
        result+=2000000
    elif a>=7 and a<=10:
        result+=500000
    elif a>=11 and a<=15:
        result+=300000
    elif a>= 16 and a<=21:
        result+=100000

    if b==1:
        result+=5120000
    elif b>=2 and b<=3:
        result+=2560000
    elif b>=4 and b<=7:
        result+=1280000
    elif b>=8 and b<=15:
        result+=640000
    elif b>=16 and b<=31:
        result+=320000
    print(result)