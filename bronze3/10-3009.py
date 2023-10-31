X =[]
Y =[]
for i in range(3):
    x1,y1 = map(int,input().split())
    X.append(x1)
    Y.append(y1)
for k in range(3):
    if X.count(X[k])==1:
        xresult = X[k]
    if Y.count(Y[k])==1:
        yresult =Y[k]
print(xresult,yresult)