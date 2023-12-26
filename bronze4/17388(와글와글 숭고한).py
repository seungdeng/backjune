S =list(map(int,input().split()))

if sum(S)>=100:
    print('OK')
else:
    if S.index(min(S))==0:
        print('Soongsil')
    elif S.index(min(S))==1:
        print('Korea')
    elif S.index(min(S))==2:
        print('Hanyang')