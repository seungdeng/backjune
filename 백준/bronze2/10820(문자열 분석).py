while 1:
    try:
        Alpha = 0
        alpha = 0 
        num = 0
        space = 0 

        sentence = input()

        for k in sentence:
            if k == ' ':
                space+=1
            elif 65<=ord(k)<=90:
                Alpha+=1
            elif 97<=ord(k)<=122:
                alpha+=1
            else:
                num+=1
        print(alpha,end=' ')
        print(Alpha,end=' ')
        print(num,end=' ')
        print(space)
    except EOFError:
        break;