#1861. 정사각형 방
delta = [(0,1),(0,-1),(1,0),(-1,0)]

def move(a, b):
    global visited
    global cnt
    global max_cnt
    visited[a][b] = True
    if max_cnt < cnt:
        max_cnt = cnt
    for dl in delta:
        nx = a + dl[0]
        ny = b + dl[1]
        if 0<= nx <N and 0<= ny <N and room[nx][ny] == room[a][b] + 1:
            cnt += 1
            move(nx,ny)
            cnt -= 1

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    temp_max = 0
    sp = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                max_cnt = 0
                cnt = 1
                move(i,j)
                if max_cnt > temp_max:
                    temp_max = max_cnt
                    sp = room[i][j]
                elif max_cnt == temp_max:
                    if sp > room[i][j]:
                        sp = room[i][j]

    print('#{} {} {}'.format(test_case, sp, temp_max))