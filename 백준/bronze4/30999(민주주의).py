n,m = map(int,input().split())

result= 0
for i in range(n):
    vote = input()
    answer = vote.count('O')
    if  answer> m//2:
        result+=1

print(result)