while 1:
    try:
        A,B = map(int,input().split())
        count = 0 
        for i in range(A,B+1):
            S = list(str(i))
            if len(set(S))==len(S):
                count+=1
        print(count)
    except EOFError:
        break