while 1:
    main = sorted(list(map(int,input().split())))
    x = set(main)
    if len(x)==1 and 0 in x :
        break
    elif main[-1]>=main[0]+main[1]:
        print('Invalid')
    elif len(x)==1:
        print('Equilateral')
    elif len(x)==2:
        print('Isosceles')
    else:
        print('Scalene')
