standard = input().split('-')
form = []

for i in standard:
    sum =0
    tmp = i.split('+')
    for j in tmp:
        sum+=int(j)
    form.append(sum)

result = form[0]

for i in range(1,len(form)):
    result -= form[i]
print(result)



# form = list(map(str,input()))
# stack = []

# result = 0
# idx =0 

# for i in form:
#     if i =='-':
#         result += int(form[idx:i])
#         idx = i
#         stack.append('-')
#     elif i=='+':
#         if stack[-1]=='-':
#             result -=int(form[idx:i])
#             idx = i
#         else :
#             result +=int(form[idx:i])
#             idx  = i

# print(result)

