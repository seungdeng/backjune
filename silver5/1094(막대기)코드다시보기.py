
CM = int(input())
X = 64
count = 0

while(True):
    if (CM<X):
        X=X//2
    else:
        CM=CM-X
        count+=1
        if(CM==0):
            break
print(count)
# X = int(input())
# count=0

# stick =[]
# stick.append(X)

# while sum(stick)>X:
#     stick.sort(reverse=0)
#     cal = stick[0]//2
#     if sum(stick)-cal >=X:
#         stick[0]=cal
#     else:
#         del(stick[0])
#         stick.append(cal)
#         stick.append(cal)
