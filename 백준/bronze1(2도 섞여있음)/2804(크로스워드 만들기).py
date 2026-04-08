A,B = list(map(str,input().split()))

Aidx = 30
for i in range(len(B)):
    if B[i] in A:
        if A.index(B[i])<Aidx:
            Aidx = A.index(B[i])
            Bidx = i

dot = '.'
dotbefore=Aidx
dotafter= len(A)-Aidx-1
for k in range(len(B)):
    if k==Bidx:
        print(A)
    else:
        print(dot*dotbefore,end='')
        print(B[k],end='')
        print(dot*dotafter)