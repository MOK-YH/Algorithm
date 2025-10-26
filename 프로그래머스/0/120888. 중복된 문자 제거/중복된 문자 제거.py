def solution(my_string):
    l = list(my_string)
    s = []
    for i in my_string:
        if i not in s:
            s.append(i) 
    return ''.join(s)