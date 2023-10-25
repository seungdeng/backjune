N = int(input())

for i in range(N):
    A = input()
    if len(A)<=9 and len(A)>=6:
        print('yes')
    else:
        print('no')