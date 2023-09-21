# from itertools import combinations, permutations
import sys
input = sys.stdin.readline
N,M = map(str,input().split())

people = []
for i in range(int(N)):
    people.append(input())
people = list(set(people))
# people.append("admin_") # 임스 리스트에 추가 
if M == 'Y': #2인
    print(len(people))    
elif M =='F': #3인
    print(len(people)//2)
elif M=='O': #4인
    print(len(people)//3)

# combi = list(combinations(people,game))

# result = 0

# for k in combi:
#     result += k.count('admin_')

# print(result)