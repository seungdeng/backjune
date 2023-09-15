import sys

N = int(input())
A =[]
for i in range(N):
    A.append(input())

A_set = list(set(A))
A_sort = []

for i in A_set:
    A_sort.append((len(i),i))

result = sorted(A_sort)

for k,j in result:
    print(j)