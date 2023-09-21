num =[]

while True:
    if num and len(num) == int(num[0])+1:
        break
    num.extend(list(map(int,input().split())))
del num[0]

for i in range(len(num)):
    num[i] = int(str(num[i])[::-1])

num.sort(reverse=False)

for i in num:
    print(i)
