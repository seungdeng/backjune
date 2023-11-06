N= int(input())
 
for i in range(N):
    quiz = input()
    count = 1
    result = 0
    for k in quiz:
        if k=='O':
            result+=count
            count+=1
        else:
            count=1
    print(result)