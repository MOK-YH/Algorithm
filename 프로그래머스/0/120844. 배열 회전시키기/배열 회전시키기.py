def solution(numbers, direction):
    answer = []
    if direction == 'right':
        k = numbers.pop()
        numbers.insert(0, k)
    else:
        k = numbers.pop(0)
        numbers.append(k)
    return numbers