N = int(input())

cow = [2]*11
count=0
for i in range(N):
    cownum,line = map(int,input().split())
    if cow[cownum] == 2:
        cow[cownum]=line
    elif cow[cownum]!=line:
        cow[cownum]=line
        count+=1
    # if line==1:
    #     if cow[cownum]==0:
    #         count+=1
    #     else:
    #         cow[cownum]=line
    # elif line==0:
    #     if cow[cownum]==1:
    #         count+=1
    #     else:
    #         cow[cownum]=line

print(count)