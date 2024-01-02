N =  int(input())

li = list(map(int,input().split()))
bbada = 0

for i in range(N):
    if i+1!=li[i]:
        bbada+=1
print(bbada)