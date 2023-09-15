def d(n):
    n = n+sum(map(int,str(n)))
    return n

self = set()

for i in range(1,10001):
    self.add((d(i)))
    
for k in range(1,10001):
    if k not in self:
        print(k)