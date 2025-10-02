def solution(numer1, denom1, numer2, denom2):
    mo = denom1 * denom2
    ja = numer1 * denom2 + numer2 * denom1
    
    best = max(mo, ja)
    gcd_value = 1
    
    for num in range(best, 0, -1):
        if mo % num == 0 and ja % num == 0:
            gcd_value = num
            break
    
    return [ja/gcd_value, mo/gcd_value]