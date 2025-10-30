def solution(s):
    t = []
    for i in s:
        if s.count(i) == 1:
            t.append(i)
    return ''.join(sorted(t))