def solution(balls, share):
    result = 1
    for i in range(share):
        result *= (balls - i)
    for i in range(1, share + 1):
        result //= i 
    return result