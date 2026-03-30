def solution(n, words):
    used = set()
    used.add(words[0])
    
    for i in range(1, len(words)):
        past = words[i-1]
        now = words[i]
        
        if now in used or past[-1] != now[0] or len(now) == 1:
            person = (i % n) + 1
            turn = (i // n) + 1
            return (person, turn)
        used.add(now)
    return [0, 0]