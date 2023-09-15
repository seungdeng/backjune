croa = ['c=','c-','d-','dz=','nj','lj','s=','z=']

n = input()

count = 0

for i in croa:
    n = n.replace(i,'*')

print(len(n))