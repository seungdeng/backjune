n = int(input())

t =[0]*36
t[0]=1


for i in range(1,len(t)):
    start= 0
    cal = i
    for k in range(i):
        t[i] += t[start]*t[cal-1]
        start+=1
        cal-=1

print(t[n])


