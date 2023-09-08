A,B,V = input().split()

A = int(A)
B = int(B)
V = int(V)

tree = 0
day = 1

while True :    
    tree += A
    if tree >= V :
        break;
    tree -= B
    day +=1

print(day)