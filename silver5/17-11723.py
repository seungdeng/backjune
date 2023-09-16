import sys
input = sys.stdin.readline
M = int(input())

S = set()

for i in range(M):
    li = input().split()
    if len(li) == 1:
        if li[0] == 'all':
            S = set(x for x in range(1,21))
        else:
            S = set()
    else:
        a,b = li[0],int(li[1])
        if a =='add':
            S.add(b)
        elif a =='check':
            if b in S:
                print(1)
            else:
                print(0)
        elif a == 'remove':
            if b in S:
                S.discard(b)
        elif a =='toggle':
            if b in S:
                S.discard(b)
            else:
                S.add(b)


# sample = []
# boolcheck = [0 for k in range(20)]

# for i in range(M):
#     sample = map(int(input().split()))

# def add(x):
#     if boolcheck[x-1] == 1:
#         return
#     else :
#         boolcheck[x-1] = 1

# def remove(x):
#     if boolcheck[x-1] ==0:
#         return
#     else :
#         boolcheck[x-1] = 0

# def check(x):
#     if boolcheck[x-1] ==1:
#         print('1')
#     else :
#         print('0')

# def toggle(x):
#     if boolcheck[x-1] == 0:
#         boolcheck[x-1] +=1
#     else:
#         boolcheck[x-1]-=1

# def all(x):
#     for j in range(M):
#         boolcheck[j] =1
# def empty(x):
#     for y in range(M):
#         boolcheck[y] = 0