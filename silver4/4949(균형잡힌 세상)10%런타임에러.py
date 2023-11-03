sstack = []
lstack = []

while 1:
    value = True
    sentence = input()
    if sentence =='.':

        exit()    
    for i in sentence:
        if i =='(':
            sstack.append(i)
        elif i=='[':
            lstack.append(i)
        elif i==')':
            if sstack[-1]=='(' and len(sstack)!=0:
                sstack.pop()
            else:
                sstack.append(i)
                break
        elif i==']':
            if lstack[-1]=='[' and len(lstack)!=0:
                lstack.pop()
            else:
                lstack.append(i)
                break
    if not sstack and not lstack:
        print('yes')
    else:
        print('no')



    # else:
    #     for i in sentence:
    #         if i == '(':
    #             middlestack.append('(')
    #         elif i =='[':
    #             largestack.append('[')
    #         elif i==')':
    #             if not middlestack:
    #                 value=False
    #                 break
    #             else:
    #                 middlestack.pop()
    #         elif i==']':
    #             if not largestack:
    #                 value:False
    #                 break
    #             else:
    #                 largestack.pop()

    # if not largestack and not middlestack:
    #     print('yes')
    # else:
    #     print('no')

