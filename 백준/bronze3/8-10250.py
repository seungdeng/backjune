T =int(input())

for i in range(T):
    H,W,N = map(int,input().split())

    floor = N % H
    room_line = (N // H) + 1
    if floor == 0:
        floor = N
        room_line -= 1
    
    print(floor * 100 + room_line)
    # result =0
    # if N-H<0:
    #     result+=1
    # else:
    #     result = 1+ (N//H)
    # if N%H ==0 :
    #     result+= 100*H
    # else:
    #     result+= (N%H)*100
    # print(result)
    num = int(input())
 
for i in range(num):
    H, W, N = map(int, input().split())
    floor = N % H
    room = N // H + 1
    if floor == 0:
        room -= 1
        floor = H
 
    print(floor*100 + room)