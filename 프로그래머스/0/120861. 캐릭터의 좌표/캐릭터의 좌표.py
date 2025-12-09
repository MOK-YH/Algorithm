def solution(keyinput, board):
    answer = [0, 0]
    limit_x = board[0] // 2
    limit_y = board[1] // 2
    for i in keyinput:
        if i == "left" and answer[0] > -limit_x:
            answer[0] += -1
        elif i == "right" and answer[0] < limit_x:
            answer[0] += 1
        elif i == "up" and answer[1] < limit_y:
            answer[1] += 1
        elif i == "down" and answer[1] > -limit_y:
            answer[1] += -1
    return answer