import re
def solution(my_string):
    answer = 0
    s = re.sub('[^0-9]', ' ', my_string)
    l = s.split()
    for i in l:
        answer += int(i)
    return answer