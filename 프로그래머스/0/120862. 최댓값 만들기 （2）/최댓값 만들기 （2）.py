def solution(numbers):
    answer = 0
    n = sorted(numbers)
    m = n[0] * n[1]
    p = n[-1] * n[-2]
    if m < p:
        answer = p
    else:
        answer = m
    return answer