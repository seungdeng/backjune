K = int(input())

x = []

for i in range(K):
    x = list(map(str,input().split()))
    del x[0]
    x.sort(reverse=False)
    print('Class '+str((i+1)))
    print("Max "+str(max(x)),end=" ")
    print("Min "+str(min(x)),end=" ")
    
    gap = int(x[1])-int(x[0])
    k=2
    for k in range(len(x)):
        if int(x[k])-int(x[k-1])>gap:
            gap = int(x[k])-int(x[k-1])
    print("Largest Gap "+str(gap))

# x = int(input())

# for i in range(x):

#     a = list(map(int, input().split()))
#     del a[0]
#     a.sort()
#     diff = []
#     print('Class', i+1)
#     for i in range(len(a)-1):
#         diff.append(a[i+1] - a[i])

#     print('Max', str(max(a))+',' ,'Min', str(min(a))+',',
#            'Largest gap', max(diff))

