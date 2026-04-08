V = int(input())

vote = input()
a = vote.count('A')
b = vote.count('B')
if a>b:
    print('A')
elif a<b:
    print('B')
else:
    print('Tie')

# vote = list(map(str,input().split()))

# a=0ㅋ7
# b=0
# for i in vote:
#     if i=='A':
#         a+=1
#     elif i=='B':
#         b+=1
# if a>b:
#     print('A')
# elif a<b:
#     print('B')
# else:
#     print()