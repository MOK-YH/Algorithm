def solution(num, k):
    l = list(str(num))
    for i in range(len(l)):
        if l[i] == str(k):
            return i +1 
    return -1