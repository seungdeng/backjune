N = input()
S = [0]*26

for i in N:
    S[ord(i)-97]+=1

for i in S:
    print(i,end=' ')