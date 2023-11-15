T = int(input())

for i in range(T):
    money= int(input())
    print(money//25,(money%25)//10,(money%25%10)//5,(money%25%10%5))