N = int(input())
check = set()
cnt=0
for i in range(N):
    S = input()
    if S == 'ENTER':
        cnt += len(check)
        check.clear()
    else:
        check.add(S)

cnt += len(check)
print(cnt)

# import sys
# input = sys.stdin.readline
# N = int(input())

# check = []
# count=0
# for i in range(N):
#     S = input().rstrip()
#     if S == 'ENTER':
#         check.clear()
#     elif S not in check:
#         check.append(S)
#         count+=1
# print(count)