X,Y = map(int,input().split())

def Rev(x):
    x = str(x)[::-1]
    x = int(x)
    return x


print(Rev(Rev(X)+Rev(Y)))

# print(Rev((Rev(X)+Rev(Y))))