A = input()
B = input()
C = input()

A = int(A)
B = int(B)
C = int(C)
j = 1
result = list(str(A*B*C))

for i in range(10):
    print(result.count(str(i)))
    