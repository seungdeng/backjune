S = input()
count = 0

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count+=1

print((count+1)//2)


# S = list(map(str,input()))

# zerocount=0
# onecount=0

# idx =0
# for i in range(1,len(S)):
#     if S[idx]!=S[i]:
#         idx = i
#         if S[idx]=='1':
#             onecount+=1
#         elif S[idx]=='0':
#             zerocount+=1
    
    
# print(min(zerocount,onecount))
