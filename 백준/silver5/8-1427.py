N = input()

A = list(map(int,N))

A.sort(reverse=True)



for i in A:
    print(i,end='')