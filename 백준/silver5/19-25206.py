rate = 0
scoreSum = 0

rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for i in range(20):
    subject, score, grade = input().split()
    if grade == "P":
        continue
    rate += float(score) * rating[grade]
    scoreSum += float(score)
    
print(rate/scoreSum)
# N = 20

# rating = ['A+','A0','B+','B0','C+','C0','D+','D0','P','F']
# grade = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0]
# where = 0

# gradetotal = 0
# result = 0

# for i in range(N):
#     a,b,c = input().split()
#     b = float(b)
#     if c !='P':
#         gradetotal += b
#         result += (b*grade[rating.index(c)])
# print('%.6f' %(result/gradetotal))


# N = 20
# a = []
# b = []
# c = []
# result = 0

# for i in range(N):
#     a,b,c = input().split()
#     b = int(b)
#     if c == 'A+':
#         c = 4.5
#     elif c=='A0':
#         c=4
#     elif c=='B+':
#         c = 3.5
#     elif c  =='B':
#         c = 3
#     elif c == 'C+':
#         c = 2.5
#     elif c == 'C':
#         c = 2
#     elif c == 'D+':
#         c = 1.5
#     elif c == 'D':
#         c == 1
#     elif c == 'P':
#         b,c =0
#     else :
#         c = 0


# for k in range(N):
#     result = (result +(b[i]*c[i]))

# result / 20

    