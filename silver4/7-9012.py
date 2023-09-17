N = int(input())

for i in range(N):
    stack = []
    a = input()
    for k in a:
        if k =='(':
            stack.append(k)
        elif k==')':
            if stack:
                stack.pop()
            else :
                print("NO")
                break
    
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
        
