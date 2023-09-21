import sys
input = sys.stdin.readline
N = input()

sequence = list(map(str,input().split()))

sequence.sort(reverse=0)


for i in range(len(sequence)-1):
    if sequence[i] == sequence[i+1]:
        print(sequence[i])
        break

import sys
N = int(input())
sumN = sum(range(1, int(N))) # n개의 수열 sumN 만들기
numbers = sys.stdin.readline().rstrip() #입력받기.근데? 공백제거
sumNum = 0 
temp = ""
for num in numbers:
    if num.isdigit(): #입력받은게 숫자면?
        temp += num # temp에 더하기
    else: #숫자가 아니면?
        sumNum += int(temp) # 
        temp = ""

# 마지막 숫자의 처리
sumNum += int(temp)

print(sumNum - sumN)