N = int(input())

time = []

for i in range(N):
    start,end = map(int,input().split())
    time.append([start,end])

time = sorted(time,key=lambda x:x[0])
time = sorted(time,key=lambda x:x[1])

endtime = 0
count =0

for x,y in time:
    if x >= endtime:
        count+=1
        endtime = y

print(count)