def solution(my_string):
    answer = []
    new_list = []
    mo = ['a', 'e', 'i', 'o' , 'u']
    new_list = list(my_string)
    for i in range(len(new_list)):
        if new_list[i] not in mo:
            answer.append(new_list[i])
    return ''.join(answer)