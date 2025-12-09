def solution(dots):
    w = []
    h = []
    for i in range(4):
        w.append(dots[i][0])
    for i in range(4):
        h.append(dots[i][1])
    w = max(w) - min(w)
    h = max(h) - min(h)
    return w * h