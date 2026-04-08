N= int(input())
S = list(map(int,input().split()))
student = int(input())
trust = True

for i in range(student):
    sex,switchnum = map(int,input().split())#a=성별 b=스위치 번호
    # 스위치 작업 남자-> 배수  
    # 여자-> 번호+ 좌우대칭 같다면
    #뒤집고 계속
    if sex==1: #남자라면
        while switchnum< N: # 배수곱할건데 인덱스 벗어나지않도록
            if S[switchnum-1]==1:
                S[switchnum-1]=0
            elif S[switchnum-1]==0:
                S[switchnum-1]=1
            switchnum=switchnum+switchnum
    elif sex==2: # 여자라면   
        if S[switchnum-1]==1:
            S[switchnum-1]=0
        elif S[switchnum-1]==0:
            S[switchnum-1]=1
        
        leftidx = switchnum-2
        rightidx = switchnum

        while trust:
            if leftidx<0 or rightidx>=N:
                # trust = False
                break
            else:
                # if S[leftidx]!=S[rightidx]:
                #     break
                # else:
                if S[leftidx]==1 and S[rightidx]==1:
                    S[leftidx]=0
                    S[rightidx]=0
                elif S[leftidx]==0 and S[rightidx]==0:
                    S[leftidx]=1
                    S[rightidx]=1
                else:
                    trust = False
                    break
                leftidx-=1
                rightidx+=1
            if trust == False:
                break
                

for i in range(len(S)):
    if (i+1)%20==0:
        print()
    print(S[i],end=' ')



