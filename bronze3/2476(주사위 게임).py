N = int(input())
result = 0

for i in range(N):
    money=0
    dice = list(map(int,input().split()))
    S =set(dice)
    if len(S)==1:
        money= 10000+(dice[0]*1000)
    elif len(S)==2:
        dice.sort(reverse=0)
        if dice[0]==dice[1]:
            money = 1000+(dice[0]*100)
        elif dice[1]==dice[2]:
            money = 1000+(dice[1]*100)
    else:
        dice.sort(reverse=1)
        money = dice[0]*100
    result = max(money,result)

print(result)