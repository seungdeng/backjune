N = int(input())
arr = []
# vs = [i for i in range(0,N+1)]
result =[]
count =1
tmp =True
for i in range(N):
    num = int(input())
    while count<=num:
        arr.append(count)
        result.append('+')
        count+=1
    if arr[-1]==num:
        arr.pop()
        result.append('-')
    else:
        tmp= False
        break

if tmp == 0:
    print('NO')
else:

    for i in result:
        print(i)


# count =1
# for i in arr:
#     while True:
#         if count<i:
#             result.append(count)
#             count+=1
#             print('+')
#         elif count==i:


