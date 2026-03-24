def solution(s):
    answer = True
    
    s = list(s)
    a = []
    
    for i in range(len(s)):
        if s[i] == '(':
            a.append(s[i])
        else:
            if a:
                a.pop()
            else:
                return False
            
    if not a:
        return True
    else: 
        return False