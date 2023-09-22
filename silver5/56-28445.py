T = set()

for q in range(2):
    a,b =map(str,input().split())
    T.add(a)
    T.add(b)

T = list(T)
T.sort(reverse=False)


for i in range(len(T)):
    for k in range(len(T)):
        print(T[i],end=" ")
        print(T[k])
        
