
dice = list(map(int,input().split()))
dice.sort(reverse=True)
check = set(dice)

if len(check) == 1:
    print(10000+(1000*dice[0]))
elif len(check) == 2:
    if dice[0]==dice[1]:
        print(1000+(dice[0]*100))
    elif dice[1]==dice[2]:
        print(1000+(dice[1]*100))
else:
    print(dice[0]*100)