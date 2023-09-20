import math

N,M = map(int,input().split(':'))

div = int(math.gcd(N,M))

print(N//div,end="")
print(":",end="")
print(M//div)