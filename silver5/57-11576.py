A,B = map(int,input().split())
m = int(input())

Aarr = list(map(int,input().split()))

sip = 0 #10진수 변환 
dan = len(Aarr)-1

for i in range(len(Aarr)):
    sip+= (A**dan)*Aarr[i]
    dan-=1

result = []
while sip//B:
    result.append(sip%B)
    sip = sip//B
result.append(sip)
result.reverse()

print(' '.join((map(str,result))))

# check = 0
# while True:
#     if B**check < sip:
#         check+=1
#     else:
#         break;

# for i in range(check+1):
#     if sip//((B)**check)!=0:
#         result = sip//((B)**check)
#     else :
#         result = sip%((B)**check)
#     print(result,end=' ')
#     check-=1
#     sip = sip-result
