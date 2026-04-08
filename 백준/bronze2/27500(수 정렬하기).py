N = int(input())
num = []

for i in range(N):
    num.append(int(input()))

num.sort(reverse=0)

for k in num:
    print(k)