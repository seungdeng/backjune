K = int(input())

li =[]
result = 0

for i in range(K):
    N = int(input())
    if (N==0):
        li.pop()
    else:
        li.append(N)



print(sum(li))