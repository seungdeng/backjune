N = int(input())

answer= []

for i in range(N):
    A = list(map(str,input()))
    if not answer:
        answer = A
    else:
        for k in range(len(A)):
            if answer[k] != A[k]:
                answer[k] = '?'


for i in answer:
    print(i,end="")