N,M = map(int,input().split())
A = [0]*N
B = [0]*M
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cha = list((set(A))&(set(B)))

print((len(A)-len(cha))+(len(B)-len(cha)))