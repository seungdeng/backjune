C = int(input())

for i in range(C):
    case = list(map(int,input().split()))
    average = sum(case[1:])//(len(case)-1)
    count = 0
    for k in range(1,len(case)):
        if case[k]> average:
            count+=1


    print(round((count/(len(case)-1))*100,3),end='')
    print('%')