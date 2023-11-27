M,N = map(int,input().split())

num ={'1':'one', '2':'two', '3':'three',
       '4':'four', '5':'five', '6':'six',
         '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

result =[]

for i in range(M,N+1):
    word = ' '.join(num[k] for k in str(i)) 
    result.append([i,word])

result.sort(key=lambda x:x[1])

for i in range(len(result)):
    if i%10==0 and result!=0:
        print()
    print(result[i][0],end=' ')
