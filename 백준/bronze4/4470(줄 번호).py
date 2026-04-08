num = int(input())
sentence =[]

for i in range(num):
    sentence.append(input())

for i in range(num):
    print(i+1,end='')
    print('. ',end='')
    print(sentence[i])