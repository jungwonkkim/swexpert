#1868. 파핑파핑 지뢰찾기
dl = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(1,1),(-1,1)]

def zero(x, y):
    global check
    check[x][y] = True
    if bomb[x][y] != 0:
        return
    for aa in range(8):
        nx = x + dl[aa][0]
        ny = y + dl[aa][1]
        if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == False and bomb[nx][ny] != '*':
            zero(nx,ny)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    bomb = [list(input()) for _ in range(N)]
    check = [[False for _ in range(N)] for _ in range(N)]
    bomb_cnt = 0
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == '.':
                cnt = 0
                for k in range(8):
                    dx = dl[k][0]
                    dy = dl[k][1]
                    if 0<=i+dx<N and 0<=j+dy<N and bomb[i+dx][j+dy] == '*':
                        cnt+=1
                bomb[i][j] = cnt
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == 0 and check[i][j] == False:
                bomb_cnt +=1
                zero(i,j)
    for a in range(N):
        for b in range(N):
            if check[a][b]== False and bomb[a][b] != '*':
                bomb_cnt +=1
    print('#{} {}'.format(test_case, bomb_cnt))