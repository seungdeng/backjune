N  = int(input())

count = 0

for i in range(N):
    word = input()
    error = 0
    for k in range(len(word)-1):
        if word[k] != word[k+1]:
            newword = word[k+1:]
            if newword.count(word[k])>0:
                error+=1
    
    if error == 0:
        count+=1
    
print(count)