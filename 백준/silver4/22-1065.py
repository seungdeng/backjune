N = int(input())

result =0


if N<100:
    result = N
else:
    result =99
    for i in range(100,N+1,1):
        i = str(i)
        if int(i[1])-int(i[0])==int(i[2])-int(i[1]):
            result+=1


print(result)