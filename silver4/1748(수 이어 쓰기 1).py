N = input()

result = 0

if len(N)==1:
    result = int(N)
else:
    result = 11
    for i in range(2,10):
        if len(N)==i:
            result +=i*(int(N)-(10**(i-1)))
            break
        else:
            result += i*(9*10**(i-1))+1
print(result)



# count=1
# for i in range(1,N+1):


# word = []
# for i in range(1,int(N)+1):
#      word.append(str(i).split())

# print(len(word))