N= int(input())
mirror = []

for i in range(N):
    mirror.append(input())
mode = int(input())

if mode==1:
    for i in mirror:
        print(i)
elif mode==2:
    for i in range(len(mirror)):
        word= mirror[i]
        print(word[::-1])
elif mode==3:
    for i in range(len(mirror)-1,-1,-1):
        print(mirror[i])
