rec = list(map(int,input().split()))

max = max(rec)
rec.remove(max)
sum = 0
result =0

for i in rec:
    sum += i

if max>=sum:
    max =sum-1
    result += sum+max
    print(result)
elif max < sum:
    print(max+sum)