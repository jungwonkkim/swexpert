#1949. [모의 SW 역량테스트] 등산로 조성
delta = [(0,1),(0,-1),(1,0),(-1,0)]


def dfs(x,y,dist):
    visited[x][y] =True
    global cut
    global max_dist
    if dist > max_dist:
        max_dist = dist
    for dl in delta:
        dx = dl[0]
        dy = dl[1]
        if 0 <= x+dx <N and 0<= y+dy < N and mountain[x][y]>mountain[x+dx][y+dy] and visited[x+dx][y+dy] ==False:
            dfs(x+dx,y+dy,dist+1)
        if cut == False:
            if 0 <= x + dx < N and 0 <= y + dy < N and mountain[x+dx][y+dy] >= mountain[x][y] > mountain[x + dx][y + dy]-K and visited[x+dx][y+dy] == False:
                cut = True
                temp = mountain[x+dx][y+dy]
                mountain[x+dx][y+dy] = mountain[x][y] -1
                dfs(x+dx,y+dy,dist+1)
                mountain[x+dx][y+dy] = temp
                cut = False
    visited[x][y] = False


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    min_val = mountain[0][0]
    max_val = 0
    max_dist = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_val:
                max_val = mountain[i][j]
            if mountain[i][j] < min_val:
                min_val = mountain[i][j]
    for a in range(N):
        for b in range(N):
            if mountain[a][b] == max_val:
                cut = False
                dfs(a,b,1)
    print('#{} {}'.format(test_case,max_dist))