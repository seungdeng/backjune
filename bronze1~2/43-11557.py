# T =int(input())

# for i in range(T):
#     N = int(input())
#     soju =0
#     for k in range(N):
#         S = input().split()
#         if int(S[1]) > soju:
#             name = S[0]
#     print(name)

T=int(input())
for i in range(T) :
    dic = {}
    N = int(input())
    for k in range(N) :
        a,b=input().split()
        dic[a]=b
    print(max(dic.keys()))
