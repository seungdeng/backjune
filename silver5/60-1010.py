import math

T = int(input())

# def factorial(x):
#     num= 1
#     for i in range(1,x+1):
#         num *=1
#     return num


# result =[0]*T
for i in range(T):
    N,M = map(int,input().split())
    void = (math.factorial(M)//(math.factorial(N)*math.factorial(M-N)))
    print(void)

# for k in result:
#     print(k)