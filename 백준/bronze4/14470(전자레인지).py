A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

result = 0
if A<0:
    while A<0:
        result+=C
        A+=1
    result+=D
    result+= E*B
elif A==0:
    result+=D
    result+= E*B
elif A>0:
    result+= E*(B-A)
print(result)