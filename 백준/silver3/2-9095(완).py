T = int(input())
N = []
result=[0]*11

result[0]=0
result[1]=1
result[2]=2
result[3]=4
for k in range(4,11,1):
    result[k] = result[k-1]+result[k-2]+result[k-3]
for i in range(T):
    N.append(int(input())) 

for j in range(len(N)):
    print(result[N[j]])  



# for i in range(T):
#     N.append(int(input()))

# for i in range(T):
#     if N[i]==1:
#         print(1)
#     elif N[i]==2:
#         print(2)
#     else:
#         print(result[N[i]])
    

