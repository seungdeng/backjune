word = list(map(str,input().split('-')))

result=[]

for i in range(len(word)):
    x = word[i]
    result.append(x[0])

print(''.join(result))