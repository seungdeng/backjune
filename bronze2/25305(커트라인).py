N,k = map(int,input().split())

score =list(map(int,input().split()))
score.sort(reverse=1)

print(score[k-1])
