def solution(array, n):
    l = []
    array.sort()
    for i in array:
        l.append(abs(n - i))
    m = min(l)
    for i in array[::-1]:
        if abs(n-i) == m:
            ans = i
    return ans