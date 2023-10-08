S = input().lower()

test = list(set(S))

countlist = []

for i in test:
    cal = S.count(i)
    countlist.append(cal)

if countlist.count(max(countlist))>=2:
    print('?')
else:
    idx = countlist.index(max(countlist))
    print(test[idx].upper())

