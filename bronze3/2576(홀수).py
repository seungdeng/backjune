num = []
for i in range(7):
    x = int(input())
    if x%2 == 1:
        num.append(x)

num.sort(reverse=0)


if not num:
    print(-1)
else:
    print(sum(num))
    print(num[0])