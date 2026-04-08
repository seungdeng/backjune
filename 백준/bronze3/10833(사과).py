N = int(input())
result =0
for i in range(N):
    school,apple=map(int,input().split())
    result += apple%school

print(result)