def solution(n):
    answer = 0
    
    for i in range(1, 6 * n +1):
        for j in range(1, 10):
            if (6 * i) % n == 0:
                return i