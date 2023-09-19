import sys
input = sys.stdin.readline
N = int(input())

li = []

for i in range(N):
    name,day,month,year = input().split()
    day,month,year = map(int(day,month,year))
    li.append((year,month,day,name)) # li[i]에 4가지 항목에 리스트로(2차원)

li.sort()

print(li[-1][3])
print(li[0][3])
