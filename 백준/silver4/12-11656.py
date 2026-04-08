S = input()
result = []

for i in range(len(S)):
    result.append(S[i:])

result.sort(reverse=0)
for k in result:
    print(k)






# S = list(map(str,input()))

# result = []


# for i in range(1,len(S)+1):
#     result.append(S[:i])


# for k in range(len(result)):
#     result[k] = ''.join(result[k])


# result.sort(reverse=0)

# for q in result:
#     print(q)