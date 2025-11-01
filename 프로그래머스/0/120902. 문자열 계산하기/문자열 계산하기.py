def solution(my_string):
    l = my_string.split()
    answer = int(l[0])
    for i in range(len(l)):
        if l[i] == "+":
            answer += int(l[i+1])
        elif l[i] == "-":
            answer -= int(l[i+1])
    return answer