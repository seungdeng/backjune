N = int(input())

num = list(map(int,input().split()))

result =0 
result+=sum(num)
result+= (len(num)-1)*8
print(result)


w