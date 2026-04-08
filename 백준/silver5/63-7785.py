import sys
import heapq
input = sys.stdin.readline
N = int(input())
name = dict()
for i in range(N):
    a = sys.stdin.readline().split()
    if a[1] == 'enter':
        name[a[0]] = 'enter'
    else:
        del name[a[0]]
name = sorted(name.keys(), reverse=True)
for i in name:
    print(i)


# name=[]

# for i in range(N):
#     a,b = map(str,input().split())
#     if b == 'enter':
#         name.append(a)
#     elif b =='leave':
#         name.pop(name.index(a))


# name.sort(reverse=1)
# print('\n'.join(name))
