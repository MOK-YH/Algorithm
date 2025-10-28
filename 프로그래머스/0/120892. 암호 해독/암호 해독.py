def solution(cipher, code):
    answer = []
    l = list(cipher)
    for i in range(code-1, len(l), code):
        answer.append(l[i])        
    return ''.join(answer)