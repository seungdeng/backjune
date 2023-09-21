import sys
input = sys.stdin.readline

N = int(input())
pizza = [0]*(11)
pizza[1] = 0
pizza[2] = 1
for i in range(3, N+1):
    div = i//2
    pizza[i] = div*(i-div) + pizza[div] + pizza[i-div]
print(pizza[N])
