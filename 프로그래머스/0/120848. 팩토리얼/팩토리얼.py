def solution(n):
    answer = 1
    for i in range(1, 15):
        answer *= i
        if answer * (i+1) > n:
            break
    return i