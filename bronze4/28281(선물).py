n,x = map(int,input().split())
N = list(map(int,input().split()))
a=N[0]
b=N[1]
result = N[0]+N[1]

for i in range(2,len(N)):
    if N[i]+N[i-1]<result:
        result = N[i] + N[i-1]
        a = N[i]
        b = N[i-1]
#차이 최소값 알아내기
print(x*a+x*b)
