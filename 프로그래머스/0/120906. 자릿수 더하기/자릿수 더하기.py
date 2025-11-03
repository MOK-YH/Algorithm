def solution(n):
    sum = 0
    l = list(str(n))
    for i in l:
        sum += int(i)
    return sum