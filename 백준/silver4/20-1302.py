N = int(input())

name = {}



for i in range(N):
    A = input()
    if A not in name:
        name[A]=1
    else:
        name[A] +=1

maxvalue = max(name.values())

bestsell = []

for key,value in name.items():
    if value == maxvalue:
        bestsell.append(key)

bestsell =sorted(bestsell)
print(bestsell[0])



