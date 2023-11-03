N = int(input())

for i in range(N):
    

# import sys
# input = sys.stdin.readline
# M = int(input())

# S = set()

# for i in range(M):
#     li = input().split()
#     if len(li) == 1:
#         if li[0] == 'all':
#             S = set(x for x in range(1,21))
#         else:
#             S = set()
#     else:
#         a,b = li[0],int(li[1])
#         if a =='add':
#             S.add(b)
#         elif a =='check':
#             if b in S:
#                 print(1)
#             else:
#                 print(0)
#         elif a == 'remove':
#             if b in S:
#                 S.discard(b)
#         elif a =='toggle':
#             if b in S:
#                 S.discard(b)
#             else:
#                 S.add(b)