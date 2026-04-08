import sys
from math import gcd
# input = sys.stdin.readline

N = int(input())
Tree = []
result = 0

start = int(input())
for i in range(N-1):    #나무사이 거리 바로 구하기
    x = int(input())
    Tree.append(x-start)
    start =x
example = Tree[0]

for k in range(1,len(Tree)):
    example = gcd(example,Tree[k])

for j in Tree:
    result += j //example-1
print(result)
