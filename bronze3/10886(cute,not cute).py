N = int(input())
cute =0
notcute = 0

for i in range(N):
    what = input()
    if what=='1':
        cute+=1
    elif what=='0':
        notcute+=1

if cute>notcute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')