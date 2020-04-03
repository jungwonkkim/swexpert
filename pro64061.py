def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        move -=1
        for i in range(len(board)):
            if board[i][move]:
                if stack:
                    if stack[-1] == board[i][move]:
                        stack.pop()
                        answer +=2
                        board[i][move] = 0
                    else:
                        stack.append(board[i][move])
                        board[i][move] = 0
                else:
                    stack.append(board[i][move])
                    board[i][move] = 0
                break
    return answer