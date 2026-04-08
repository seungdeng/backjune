import math
L = int(input())
A = int(input())
B= int(input())
C = int(input())
D = int(input())
mathday = math.ceil(A/C)
korean = math.ceil(B/D)

print(L-max(mathday,korean))