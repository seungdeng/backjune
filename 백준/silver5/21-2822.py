score = []
sample = []

value = 0

for i in range(8):
    score.append(int(input()))

for i in range(5):
    sample.append((score.index(max(score)+1)))
    value += score[score.index(max(max(score)))]
    score[score.index(max(score))]=0

sample.sort()
print(score)

for k in sample:
    print(k,end = " ")

# A =[]
# B = []
# C = []

# for i in range(8):
#     A = input()

# B = int(A)

# B.sort()

# for k in range(5):
#     C = int(A.index(B[k]))

# C.sort()

# for j in range(5):
#     print(C[j],end = " ")