#4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

def maze(a, b):
    if maps[a][b] == 3:
        global result
        result = 1
        return
    elif result == 1:
        return
    else:
        global visited
        visited[a][b] = 1
        if a + 1 < N and maps[a + 1][b] != 1 and visited[a + 1][b] == 0:
            maze(a + 1, b)
        if a > 0 and maps[a - 1][b] != 1 and visited[a - 1][b] == 0:
            maze(a - 1, b)
        if b + 1 < N and maps[a][b + 1] != 1 and visited[a][b + 1] == 0:
            maze(a, b + 1)
        if b > 0 and maps[a][b - 1] != 1 and visited[a][b - 1] == 0:
            maze(a, b - 1)
        visited[a][b] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maps = [list(map(int,input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                maze(i,j)
    print('#{} {}'.format(test_case, result))
