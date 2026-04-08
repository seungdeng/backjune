M,N = map(int,input().split())

A = []



for M in range(N+1):
    i = 2
    count = 0
    while M>i:
        if M%i==0:
            count+=1
            break
        i+=1
    if count==0:
        A.append(M)

for k in A:
    print(k)

#     def isPrime(num):
#     if num==1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 return False
#         return True

# M, N = map(int, input().split())

# for i in range(M, N+1):
#     if isPrime(i):
#         print(i)