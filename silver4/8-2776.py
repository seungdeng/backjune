import sys
input = sys.stdin.readline

T = int(input())

for k in range(T):
    N = int(input())
    A = set(map(int,input().split()))
    M = int(input())
    B = list(map(int,input().split()))
    for i in B:
        if i in A:
            print("1")
        else:
            print("0")