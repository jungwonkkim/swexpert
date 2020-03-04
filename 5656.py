import copy

delta = [(1,0),(-1,0),(0,1),(0,-1)]


def shoot(status, zone, time):
    global min_left

    if min_left == 0:
        return

    for a in range(H):
        if sum(status[a]):
            break
    else:
        min_left = 0
        return

    if time == 0:
        cnt = 0
        for i in range(H):
            if cnt > min_left:
                break
            for j in range(W):
                if status[i][j]:
                    cnt += 1
        if min_left > cnt:
            min_left = cnt
        return

    stack = []
    for check in range(H):
        if status[check][zone]:
            stack.append((check, zone))
            break
    else:
        return

    while stack:
        x, y = stack.pop()
        for dist in range(status[x][y]):
            for dl in delta:
                nx = x + (dl[0]*dist)
                ny = y + (dl[1]*dist)
                if (nx,ny) not in stack and -1<nx<H and -1<ny<W and status[nx][ny]:
                    stack.append((nx,ny))
        status[x][y] = 0

    for i in range(W):
        for j in range(1, H):
            if status[j][i] == 0:
                for k in range(j,0,-1):
                    status[k][i] = status[k-1][i]
                status[0][i] = 0

    for next in range(W):
        new_status = copy.deepcopy(status)
        shoot(new_status, next, time-1)



T = int(input())

for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    min_left = W * H
    for sp in range(W):
        board_case = copy.deepcopy(board)
        for rr in range(H):
            if board_case[rr][sp]:
                shoot(board_case, sp, N)
                break
    print('#{} {}'.format(test_case, min_left))