# import sys
# input = sys.stdin.readline
N = int(input())
card = sorted(list(map(int,input().split())))
M = int(input())
check = list(map(int,input().split()))

count= {}

for i in card:
    if i in count:
        count[i] +=1
    else:
        count[i] =1

for k in check:
    if k in count:
        print(count[i],end = ' ')
    else:
        print(0,end=' ')
    # result = count.get(k)
    # if result == None:
    #     print(0,end=' ')
    # else:
    #     print(result,end=' ')
# N  = int(input())
 
# S = list(map(int,input().split()))

# M = int(input())

# result = [0]*M

# Y = list(map(int,input().split()))

# for i in range(N):
#     if S[i] in Y:
#         k = Y.index(S[i])
#         result[k]+=1

# print(' '.join(map(str,result)))

from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

hash = {}

for i in card:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in test:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')