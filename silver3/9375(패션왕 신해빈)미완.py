from itertools import combinations
T = int(input())

wear =[]
body = []


for i in range(T):
    N = int(input())
    result = 0
    for k in range(T):
        a,b = map(str,input().split())
        wear.append(a)
        body.append(b)
    result = len(a)+len(b)
    result += combinations(len(a),len(b))
