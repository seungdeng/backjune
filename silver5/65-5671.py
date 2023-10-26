T = int(input())

for i in range(T):
    N = int(input())
    C = list(map(int,input().split()))
    count =0
    while True:
        C = [i+1 if i%2 else i for i in C]
        if len(set(C)) == 1:
            print(count)
            break
        C = [C[i] // 2+C[(i+1)%N]//2 for i in range(N)]
        count+=1