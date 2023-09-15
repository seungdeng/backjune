N = int(input())

A = []
for i in range(N):
    age,name = map(str,input().split())

    age = int(age)
    A.append([age,i,name])

A.sort()

for i in range(len(A)):
    print(A[i][0], A[i][2])
