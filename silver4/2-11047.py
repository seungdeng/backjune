N,K = map(int,input().split())

price= []

count = 0

for i in range(N):
    price.append(int(input()))

price.sort(reverse=True)

for j in price:
    count += K//j
    K = K%j

print(count)