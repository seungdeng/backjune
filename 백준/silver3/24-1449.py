N,L =map(int,input().split())
water = sorted(list(map(int,input().split())))
count  = 1
start = water[0]

for i in water[1:]:
    if (i+0.5)-(start-0.5)<=L:
        continue
    else:
        count+=1
        start = i
print(count)


