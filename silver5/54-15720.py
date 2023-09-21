B,C,D = map(int,input().split())

result =0

burger = list(map(int,input().split()))
side = list(map(int,input().split()))
drink =list(map(int,input().split())) 
# max = max(len(burger),len(side),len(drink))
min = min(B,C,D)

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)
for x in range(min):
    result += ((burger[x]+drink[x]+side[x])*9)//10

result+= sum(burger[min::])
result += sum(side[min::])
result += sum(drink[min::])

print(sum(burger)+sum(side)+sum(drink))
print(result)


