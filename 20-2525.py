A,B = input().split()
C = input()
A = int(A)
B = int(B)
C = int(C)

A += int(C/60)
B += C%60

if B>=60:
    A+=1
    B-=60

if A >=24:
    A-=24

print(A,B)
