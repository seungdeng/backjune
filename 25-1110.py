N  = int(input())

compare = N
cycle = 0

while True:
    A = compare //10
    B = compare % 10
    C = (A+B) % 10
    compare = (B*10)+C

    cycle +=1
    if (compare == N):
        break;

print(cycle)
