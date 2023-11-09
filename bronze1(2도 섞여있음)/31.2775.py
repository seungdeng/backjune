# T = int(input())

# for i in range(T):
#     floor = int(input())
#     num = int(input())
#     f = [x for x in range(1,num+1)]
#     for j in range(floor):
#         for k in range(1,num):
#             f[i] +=f[i-1]

#         print(f)
#     print(f[-1])

T = int(input())

# def solution(a,b):
#     people= 0
#     for i in range(1,b):
#         people +=i
#     print((a+1)*people)

for i in range(T):
    people=0
    k= int(input())
    n = int(input())
    if k ==1:
        for i in range(1,n+1):
            people +=i
    print(people)
    else:
        

