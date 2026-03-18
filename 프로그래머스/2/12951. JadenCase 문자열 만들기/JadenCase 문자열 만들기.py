def solution(s):
    answer = []
    
    for word in s.split(" "):  # 공백 유지 핵심
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append("")  # 공백 유지
    
    return " ".join(answer)