A = []

A = list(map(str,input().split()))

B = [0,0,0,0]

result = 0

for i in range (len(A)):
    if A[i][0] == 'U' and B[1]==0 and B[2] ==0 and B[3] == 0:
        B[0]+=1
    elif A[i][0] =='C' and B[0] >0 and B[2] ==0 and B[3] ==0:
        B[1] +=1
    elif A[i][0] =='P' and B[0] >0 and B[1] >0 and B[3] ==0:
        B[2] +=1
    elif A[i][0] == 'C' and B[0]>0 and B[1]>0 and B[2] >0:
        B[3] +=1

if not 0 in B:
    print('I love UCPC')
else:
    print('I hate UCPC')

    import sys

# s = sys.stdin.readline()
# check_list = ['U', 'C', 'P', 'C']
# isSuccess = True

# for check in check_list:
#     if check in s:
#         s = s[s.find(check)+1:]
#     else:
#         isSuccess = False
#         break

# if isSuccess:
#     print("I love UCPC")
# else:
#     print("I hate UCPC")
