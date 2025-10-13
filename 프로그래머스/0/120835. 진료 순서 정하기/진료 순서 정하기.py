def solution(emergency):
    answer = []
    emerge = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(emerge.index(i)+1)
    return answer