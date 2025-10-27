def solution(order):
    l = list(str(order))
    m = '3', '6', '9'
    cnt = 0
    for i in l:
        if i in m:
            cnt += 1
    return cnt