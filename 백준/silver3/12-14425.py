N,M = map(int,input().split())

dic = {}
count = 0 

for i in range(N):
    A = input().rstrip()
    dic[A] = 1

for k in range(M):
    A = input().rstrip()
    if A in dic:
        count+=1

print(count)
# for i in range(N):
#     dic[input()] = 0

# for k in range(M):
#     dic[input()] = 1

# print(sum(dic.values()))




