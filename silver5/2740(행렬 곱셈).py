a1,b1 = map(int,input().split())
A = []
B = []
for i in range(a1):
    A.append(list(map(int,input().split())))

a2,b2 = map(int,input().split())

for i in range(a2):
    B.append(list(map(int,input().split())))

cal = [[0 for i in range(b2)]for i in range(a1)]

for i in range(a1):
    for j in range(b2):
        for k in range(b1):
            cal[i][j] += A[i][k]*B[k][j]

for i in cal:
    for j in i:
        print(j,end=' ')
    print('')


# for i in range(a1):
#     for j in range(b2):
#         print(A[i][j]*B[i][j])