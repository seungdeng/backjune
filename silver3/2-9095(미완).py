T = int(input())
N = []
result=[0 for i in range(11)]

result[0]=0
result[1]=1
result[2]=2

for k in range(3,11,1):
    result[k] = result[k-1]+result[k-2]+result[k-3]
# def solution(a):
    
#     if a==1:
#         print(result[1])
#     elif a==2:
#         print(result[2])
#     else:
#         print(result[a])
    

for i in range(T):
    N.append(int(input()))

for i in range(T):
    if N[i]==1:
        print(1)
    elif N[i]==2:
        print(2)
    else:
        print(result[N[i]])
    

