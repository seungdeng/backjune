S =[]

for i in range(28):
    S.append(int(input()))
result = []

for k in range(1,31):
    if k not in S:
        result.append(k)

for j in range(len(result)):
    print(result[j])