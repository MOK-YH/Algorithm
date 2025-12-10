def solution(polynomial):
    answer = ''
    xx = ''
    sums = 0
    sumx = 0
    
    p = polynomial.split(" + ")
    
    for i in p:
        if "x" in i:
            if i == "x":
                sumx += 1
            else:
                sumx += int(i.replace("x",""))
        else:
            sums += int(i)

    if sumx == 0:
        answer = str(sums)
    elif sums == 0:
        if sumx == 1:
            answer = "x"
        else:
            answer = str(sumx) + "x"
    else:
        if sumx == 1:
            xx = "x"
        else:
            xx = str(sumx) + "x"
        answer = xx + " + " + str(sums)
    return answer