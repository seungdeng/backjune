N= int(input())
S = list(map(int,input().split()))
student = int(input())

for i in range(student):
    a,b = map(int,input().split())#a=성별 b=스위치 번호
    # 스위치 작업 남자-> 배수  
    # 여자-> 번호+ 좌우대칭 같다면
    #뒤집고 계속
    if a==1: #남자라면
        while b< N: # 배수곱할건데 인덱스 벗어나지않도록
            if S[b-1]==1:
                S[b-1]=0
            elif S[b-1]==0:
                S[b-1]=1
            b=b+b
    elif a==2: # 여자라면   
        if S[b-1]==1:
            S[b-1]=0
        elif S[b-1]==0:
            S[b-1]=1
        
        leftidx = b-2
        rightidx = b
        while 1:
            if leftidx<0 or rightidx>=N:
                break
            else:
                if S[leftidx]!=S[rightidx]:
                    break
                else:
                    if S[leftidx]==1:
                        S[leftidx]=0
                        S[rightidx]=0
                    elif S[leftidx]==0:
                        S[leftidx]=1
                        S[rightidx]=1
                    leftidx-=1
                    rightidx+=1

for i in S:
    print(i,end=' ')

