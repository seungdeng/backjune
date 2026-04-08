x,y = map(int(input().split()))

def gcd(x,y):
    while x>0:
        x,y = y,x%y

    return x

def lcm(x,y):
    return x*y

print(gcd(x,y))
print(lcm(x,y))


