result =int(input())

word = input()

sdsd= []
for i in range(len(word)):
    sdsd.append(word[i])

s = sdsd.count('s')
t = sdsd.count('t')

while 1:
    if s==t:
        break;
    else:
        del(sdsd[0])
        s = sdsd.count('s')
        t = sdsd.count('t')
        

for i in sdsd:
    print(i,end='')
    # 소떧소떡 출력