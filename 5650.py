#5650. [모의 SW 역량테스트] 핀볼 게임
delta = [(-1,0),(1,0),(0,-1),(0,1)] #상 하 좌 우
block = [(), (1,3,0,2), (3,0,1,2),(2,0,3,1),(1,2,3,0),(1,0,3,2)]
def pinball(a, b, di):
    global max_score
    cnt = 0
    newa = a + delta[di][0]
    newb = b + delta[di][1]
    x, y, d = newa, newb, di
    while True:
        if x == a and y == b:
            break
        if -1<x<N and -1<y<N:
            if game_board[x][y] == -1:
                break
            if game_board[x][y] == 0:
                x = x + delta[d][0]
                y = y + delta[d][1]
                continue
            if 1<=game_board[x][y]<=5:
                cnt +=1
                d = block[game_board[x][y]][d]
                x = x + delta[d][0]
                y = y + delta[d][1]
                continue
            if (x, y) == wormhole_list[0][game_board[x][y] - 6]:
                x, y = wormhole_list[1][game_board[x][y] - 6]
                x = x+delta[d][0]
                y = y+delta[d][1]
                continue
            x, y = wormhole_list[0][game_board[x][y] - 6]
            x = x+delta[d][0]
            y = y+delta[d][1]
            continue
        else:
            cnt +=1
            if x <0:
                x = 0
                d = 1
                continue
            if x == N :
                x = N-1
                d = 0
                continue
            if y < 0 :
                y = 0
                d = 3
                continue
            y = N-1
            d = 2
            continue
    if max_score < cnt:
        max_score = cnt
    return

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    game_board = [list(map(int, input().split())) for _ in range(N)]
    wormhole_list = [[0 for _ in range(5)] for _ in range(2)]
    for a in range(N):
        for b in range(N):
            if game_board[a][b] >=6:
                if wormhole_list[0][game_board[a][b]-6]:
                    wormhole_list[1][game_board[a][b]-6] = (a, b)
                else:
                    wormhole_list[0][game_board[a][b]-6] = (a, b)
    max_score = 0
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0:
                for direction in range(4):
                    pinball(i, j, direction)
    print('#{} {}'.format(test_case, max_score))