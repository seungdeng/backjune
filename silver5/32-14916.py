n = int(input())

count5 = 0
count2 = 0

while True:
    if n==1 or n==3:
        count5-=1
        break;
    elif n%5==0 or n%5 ==2 or n%5 == 4:
        count5 = int(n/5)
        count2 = int((n%5)/2)
        break;
    else:
        count5 = int(n/5)-1
        count2 = int(((n%5)+5)/2)
        break;

print(count5+count2)


# n = int(input())

# count = 0
# while True:
#     if n%5 ==0:
#         count += (n//5)
#         break
#     else : 
#         n -=2
#         count +=1
#     if n<0:
#         break;
# if n<0:
#     print("error")
# else:
#     print(count)




# n = int(input())    # 거스름돈 액수 n
 
# tmp = n % 5 # 반복해서 나오는 식을 간단하게 변수로 선언해두기
 
# if n == 1 or n == 3:    # 거스름돈이 1이나 3이면 거슬러줄 수 없으므로 -1 출력
#     print(-1)
 
# elif tmp % 2 == 0:  # n이 5로 나누었을 때의 나머지가 짝수이면(2로 나눌 수 있으면)
#     print((n // 5) + (tmp // 2))  # 5로 나눴을 때의 몫 + 그 나머지를 2로 나눴을 때의 몫.
 
# else:   # n이 5로 나누었을 때의 나머지가 홀수이면(2로 나눌 수 없음)
#     print((n // 5) - 1 + (tmp + 5) // 2) 