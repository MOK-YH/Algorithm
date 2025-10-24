def solution(my_string):
    answer = 0
    my_list = list(my_string)
    for i in range(len(my_list)):
        if my_list[i].isdigit():
            answer += int(my_list[i])
    return answer