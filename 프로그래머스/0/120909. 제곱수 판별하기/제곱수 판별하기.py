def solution(n):
    for i in(range(1, int(n/2))):
        if n % i == 0:
            if i * i == n:
                return 1
    return 2