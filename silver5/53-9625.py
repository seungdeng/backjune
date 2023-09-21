K = int(input())
n =46
A = [0]*46
A[0] = 1
A[1] = 0
B = [0]*46
B[0] = 0
B[1] = 1

for i in range(2,n,1):
    A[i] = A[i-2] + A[i-1]
    B[i] = B[i-2] + B[i-1]

print(A[K],B[K])


# if K==1:
#     A =[0,1]
# else:
#     i=2
#     for i in range(K+1):
#         temp=A[0]
#         A[0] = A[1]
#         A[1] += temp
# print(A)



# mon = ['A']

# for i in range(K):
#     for j in range(len(mon)):
#         if mon[j] =='A':
#             mon[j] = 'B'
#         elif mon[j] =='B':
#             mon[j:j] = 'A','B'
#             j+=1

# countA = 0
# countB = 0

# countA = mon.count('A')
# countB = mon.count('B')

# print(countA,countB)



