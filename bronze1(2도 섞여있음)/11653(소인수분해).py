def solution(x):
    num = 2
    while num<=x:
        if x%num==0:
            print(num)
            x = x//num
        else:
            num+=1


N = int(input())
if N>=2:
    solution(N)
