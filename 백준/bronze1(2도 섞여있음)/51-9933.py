N = int(input())

Words = [input() for i in range(N)]

for j in Words:
    if j[::-1] in Words:
        print(len(j),end=' ')
        print(j[len(j)//2])
        exit()

