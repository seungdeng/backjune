n =int(input())
p = int(input())
price = []

if n<5:
    print(p)
elif n<10:
    if p-500<0:
        print(0)
    else:
        print(p-500)
elif n<15:
    price.append(p-500)
    price.append(p*90//100)
    result = min(price)
    if result <0:
        print(0)
    else:
        print(result)
elif n<20:
    price.append(p-2000)
    price.append(p*90//100)
    result = min(price)
    if result<0:
        print(0)
    else:
        print(result)
else:
    price.append(p-2000) 
    price.append(p*75//100)
    result = min(price)
    if result<0:
        print(result)
    else:
        print(result)
    #