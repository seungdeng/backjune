import math
N = list(map(int,input()))

compare = [0,1,2,3,4,5,6,7,8,9]
count = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(N)):
    if N[i] == 6 or N[i] ==9:
        if count[6] <= count[9]:
            count[6] +=1
        else :
            count[9] +=1
    else:
        count[N[i]]+=1


count.sort(reverse=True)

print(count[0])


# for i in range(len(N)):
#     for k in range(9):
#         if N[i] == compare[k]:
#             count[k] +=1

# count[6] = math.ceil((count[6]+count[9])/2)
# count[9] = 0

# count.sort(reverse=True)
# print(count[0])



