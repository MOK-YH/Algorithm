def solution(n):
    cnt = 0
    for i in range(1, n + 1):
        divisor = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisor += 1
        if divisor >= 3:  # 약수가 3개 이상이면 합성수
            cnt += 1
    return cnt
