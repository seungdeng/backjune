dic = {'A':2,'B':2,'C':2,'D':3,'E':3,
       'F':3,'G':4,'H':4,'I':4,'J':5,
       'K':5,'L':5,'M':6,'N':6,'O':6,
       'P':7,'Q':7,'R':7,'S':7,'T':8,
       'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9}

x = input()

y = []

result = 0

for i in range(len(x)):
    y.append(dic[x[i]] + 1)


for j in range(len(y)):
    result = result + y[j]

print(result)


d = {"ABC":3,"DEF":4,"GHI":5,"JKL":6,"MNO":7,"PQRS":8,"TUV":9,"WXYZ":10}
cnt=0
num =input()
for n in num:
    for j in d.keys():
        if str(n) in j:
            cnt +=d.get(j)
print(cnt)

