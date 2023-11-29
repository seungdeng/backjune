N,b = input().split()

setting = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = N[::-1]
result = 0

for i,j in enumerate(N):
    result += (int(b)**i)*(setting.index(j))

print(result)