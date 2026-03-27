def solution(name, yearning, photo):
    
    answer = []
    dt = dict(zip(name, yearning))
    
    for i in photo:
        temp = list(set(name) & set(i))
        exist = sum([dt[k] for k in temp if k in dt])
        answer.append(exist)
                     
    return answer