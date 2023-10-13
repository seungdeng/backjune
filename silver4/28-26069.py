N = int(input())

check = set()
check.add('ChongChong')


for i in range(N):
    a,b = map(str,input().split())
    if a in check:
        check.add(b)
    elif b in check:
        check.add(a)

print(len(check))

