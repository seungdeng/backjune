import sys
input = sys.stdin.readline
from collections import Counter
N = int(input())
S = []

for i in range(N):
    S.append(int(input()))

print(round(sum(S)/N)) #산술평균
print(sorted(S)[len(S)//2]) # 중앙값 
cnt = {}

for k in range(N):
    if S[k] not in cnt.keys():
        cnt[S[k]] =1
    else:
        cnt[S[k]] +=1       

cnt = sorted(cnt.items(),key=lambda x:(-x[1],x[0]))
for i in range(len(cnt)):
    cnt[i] = list(cnt[i])
if len(cnt) == 1 or cnt[0][1] != cnt[1][1]:
    print(cnt[0][0])
else:
    print(cnt[1][0])


# mostS = Counter(S).most_common(2)
# if mostS[0][1] == mostS[1][1]:
#     print(mostS[1][0])
# else:
#     print(mostS[0][0])# 최빈값, 시간초과로 인해 counter 활용(2트,시간초과)
# check = {}
# for i in S:
#     if i in check:
#         check[i] +=1
#     else:
#         check[i] = 1
# maxnum = max(check.values())
# maxS = []
# for k in check:
#     if maxnum == check[k]:
#         maxS.append(k)

# if len(maxS)>1:
#     print(maxS[1])
# else:
#     print(maxS[0])# 최빈값

print(max(S)-min(S))# 최댓값과 최솟값의 차이 