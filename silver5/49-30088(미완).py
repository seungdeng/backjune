N = int(input())

A =[]
result = []
for i in range(N):
    A= (map(int,input().split()))
    result.append(sum(A[1:]))
    
result.sort(reverse=True)
cal = 0
su =-1
for k in range(len(result)):
    cal += sum(result[su:])
    su-= -1

# hap = 0

# for i in result:
#     for k in i :
#         hap += i

# print(hap)

