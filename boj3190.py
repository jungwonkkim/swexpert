#백준 3190 뱀
delta = [(0,1), (1, 0), (0,-1),(-1,0)]
N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
snake = [[0,0]]
d = 0
cnt = 0
stop = False
for apple in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
L = int(input())
change = []
for l in range(L):
    X, C = input().split()
    X = int(X)
    if l:
        for j in range(l):
            X -= change[j][0]
    change.append((X, C))
for ch in change:
    if stop:
        break
    for i in range(ch[0]):
        cnt += 1
        new_snake = [snake[-1][0]+delta[d][0], snake[-1][1]+delta[d][1]]
        if 0<=new_snake[0]<N and 0<=new_snake[1]<N and new_snake not in snake:
            snake.append(new_snake)
            if board[new_snake[0]][new_snake[1]]==0:
                del snake[0]
            else:
                board[new_snake[0]][new_snake[1]] = 0
        else:
            stop = True
            break
    if ch[1] == "L":
        d = (d-1)%4
    else:
        d = (d+1)%4
if stop == False:
    while True:
        cnt +=1
        new_snake = [snake[-1][0] + delta[d][0], snake[-1][1] + delta[d][1]]
        if 0 <= new_snake[0] < N and 0 <= new_snake[1] < N and new_snake not in snake:
            snake.append(new_snake)
            if board[new_snake[0]][new_snake[1]] == 0:
                del snake[0]
            else:
                board[new_snake[0]][new_snake[1]] = 0
        else:
            stop = True
            break

print(cnt)

