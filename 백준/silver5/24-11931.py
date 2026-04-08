import sys
input = sys.stdin.readline

N = int(input())

a = []
for i in range(N):
    a.append(int(input()))


a.sort(reverse=True)

for k in range(len(a)):
    print(str(a[k]))