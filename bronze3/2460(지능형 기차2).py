people=0
result=0
for i in range(10):
    minus,plus = map(int,input().split())
    result=max(result,people-minus+plus)
    people = people-minus+plus
print(result)
