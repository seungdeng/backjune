N = int(input())

num = sorted(list(map(int,input().split())))

result = num[0]*num[-1]
print(result)