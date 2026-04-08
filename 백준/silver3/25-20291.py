import sys
input = sys.stdin.readline

N = int(input())
dict = {}
type = []


for i in range(N):
    word = input().split('.') 
    type.append(word[1])
for k in type:
    if k in dict:
        dict[k]+=1
    else:
        dict[k]=1

    # if word[1] in dict:
    #     dict[word[1]]+=1
    # else:
    #     dict[word[1]]=1
dict = sorted(dict.items(),key=lambda x:(x[0],x[1]))
for i in dict:
    print(i[0],i[1])