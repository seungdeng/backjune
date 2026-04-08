N = int(input())


for i in range(N):
    A = list(map(str,input()))

    line = int(len(A)**0.5)

    result = []

    for j in range(line):
        cal = line*(line-1)
        cal+=j
        for k in range(line):
            result.append(A[cal])
            cal-=line

    result.reverse()    
    print(''.join((map(str,result))))


    
    
