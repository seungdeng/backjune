import sys
N = int(input())

A= []

for i in range(N):
    A.append(int(input()))

count= 0
while True:
    if A[0]>max(A[1:]):
        break
    k = A.index(max(A))
    A[k] -=1
    A[0] +=1
    count +=1

print(count)

# N = int(input())
# dasom = int(input())
# A = []
# count =0

# for i in range(N-1):
#     A.append(int(input()))
# A.sort(reverse=True)

# if N ==1:
#     print('0')
# else:
#     while A[0] >= dasom:
#         dasom+=1
#         A[0] -=1
#         count +=1
#         A.sort(reverse=True)
#     print(count)
