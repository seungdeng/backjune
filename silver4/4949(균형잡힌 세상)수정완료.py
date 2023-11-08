import sys
input = sys.stdin.readline

while 1:
    stack = []
    stack = []
    sentence = input().rstrip()
    if sentence == '.':
        exit()
    for i in sentence:
        if i =='(' or i=='[':
            stack.append(i)
        elif i==')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i==']':
            if len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(i)
                break
    if not stack :
        print('yes')        
    else:
        print('no')























    # value = True
    
    
    # sstack = []
    # lstack = []
    # sentence = input().rstrip()
    # if sentence == '.':
    #     exit()
    # for i in sentence:
    #     if i =='(':
    #         sstack.append(i)
    #     elif i=='[':
    #         lstack.append(i)
    #     elif i==')':
    #         if len(sstack)!=0 and sstack[-1]=='(':
    #             sstack.pop()
    #         else:
    #             sstack.append(i)
    #             break
    #     elif i==']':
    #         if len(lstack)!=0 and lstack[-1]=='[':
    #             lstack.pop()
    #         else:
    #             lstack.append(i)
    #             break
    # if not sstack and not lstack:
    #     print('yes')
        
    # else:
    #     print('no')


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

