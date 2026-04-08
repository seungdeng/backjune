a,b = map(int,input().split())

k,x = map(int,input().split())

low = k-x
high = k+x
count = 0
for i in range(a,b+1):
    if i>=low and i<=high:
        count+=1

if count==0:
    print('IMPOSSIBLE')
else:
    print(count)