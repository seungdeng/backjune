N= int(input())
S = list(map(int,input().split()))
student = int(input())

for i in range(student):
    a,b = map(int,input().split())#a=성별 b=스위치 번호

    # 스위치 작업 남자-> 배수  
    # 여자-> 번호+ 좌우대칭 같다면
    #뒤집고 계속
