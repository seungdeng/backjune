color = {'black':0,'brown':1,'red':2,'orange':3,
         'yellow':4,'green':5,'blue':6,'violet':7,
         'grey':8,'white':9}

one = input()
two = input()
num = input()
result = 0

result += color[one]*10
result += color[two]
result *= 10**color[num]

print(result)