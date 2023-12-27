Xa = int(input())
Yb = int(input())
Yc = int(input())
Yd = int(input())
P = int(input())

result = []

result.append(Xa*P)
y = 0
if P<=Yc:
    y = Yb*P
else:
    y += Yb*Yc
    y += (P-Yc)*Yd
result.append(y)

print(min(result))