def solution(hp):
    cnt = 0
    cnt += hp // 5
    cnt += (hp % 5) // 3
    cnt += (hp % 5) % 3
    return cnt