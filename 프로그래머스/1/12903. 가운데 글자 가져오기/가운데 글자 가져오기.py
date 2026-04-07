def solution(s):
    
    answer = list(s)
    
    if len(answer) % 2 == 0:
        
        
        return answer[len(answer)//2-1]+answer[len(answer)//2]
    else:
        return answer[len(answer)//2]
