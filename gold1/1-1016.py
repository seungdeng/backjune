a, b = map(int, input().split())
li = [1]*(b-a+1)
for i in range(2, int(b**0.5)+1):
    t = i**2
    for j in range(a//t*t, b+1, t):
        if j-a >= 0 and li[j-a]:
            li[j-a] = 0
print(li.count(1))


# min,max = map(int,input().split())
# i = min
# count = 0

# def zegop(x):
#     return x**2

# for i in range(max+1):
#     zegopsu = 2
#     while zegop(zegopsu)<=i:
#         if i%zegop(zegopsu) ==0:
#             zegopsu+=1
# else:

