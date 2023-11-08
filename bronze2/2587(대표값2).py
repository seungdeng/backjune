num = []

for i in range(5):
    num.append(int(input()))
num.sort(reverse=0)

print(sum(num)//5)
print(num[2])
