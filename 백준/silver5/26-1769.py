X = input()
count = 0

while len(X)>=2:
    sum = 0
    for i in range(len(X)):
        sum +=int(X[i])
    X = str(sum)
    count+=1

print(count)
if int(X)%3==0:
    print("YES")
else :
    print("NO")    

# X  = list(map(int,input()))

# count = 0

# cal = sum(X)

# def solution(n):            # 시간복잡도 : 4n + 3 = O(n)
#     answer = 0              # 대입연산 : 1
#     for i in str(n):        # 반복문, str 변환 : n + 1 
#         answer += int(i)    # 대입연산, 덧셈연산, int 변환 : 3n
#     return answer  

# while True:
#     if cal<10:
#         break;
#     solution(X)
#     count+=1


# print(str(count))
# if X%3==0:
#     print("YES")
# else:
#     print("NO")

    