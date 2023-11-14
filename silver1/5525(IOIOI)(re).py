N = int(input())
M = int(input())
S = input()

result = 0
count = 0
i = 0

while i<(M-1):
    if S[i:i+3]=='IOI':
        i+=2
        count+=1
        if count==N:
            result+=1
            count-=1
    else:
        i+=1
        count=0

print(result)


# N = int(input())
# M = int(input())
# S = input()
# P = 'IO'*N + 'I'
# answer = 0

# for i in range(M - len(P)):
#     if S[i] == 'I':
#         if S[i:i+len(P)] == P:
#             answer += 1
# print(answer)
#런타임에러

# Pn = ['I']
# for i in range(N):
#     Pn.append('O')
#     Pn.append('I')


# print(S)