import sys
input = sys.stdin.readline
N = input()[::-1]

result = ''
temp = 0
count =1

for i in N:
    if (count<8):
        temp += count * int(i)
        count *=2
    else:
        result += str(temp)
        temp = 1*int(i)
        count = 2
result +=str(temp)
print(int(result[::-1]))

# N = list(map(int,input()))

# result=[]


# if len(N)%3==0:
#     while not N:
#         result.append((N.pop()+N.pop()+N.pop()))

# result.reverse()
# print(result)
# # for i in range(len(N)):
# #     if N[i] == 1:
# #         sip += 2**(len(N)-i-1)






