N =int(input())
A = [0]*N

for i in range(len(A)):
    A[i] = int(input())

count =0
k = N-1
while 1:
    if k == 0:
        break
    elif A[k]<=A[k-1]:
        A[k-1]-=1
        count+=1
    elif A[k]>A[k-1]:
        k-=1

print(count)
    