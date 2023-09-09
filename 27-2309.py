a =[]

for i in range (9):
    a.append(int(input()))

a.sort(reverse=False)

for i in range(9):
    print(a[i])