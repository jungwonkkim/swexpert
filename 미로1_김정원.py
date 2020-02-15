#1226. [S/W 문제해결 기본] 7일차 - 미로1

def dfs(a,b):
    if maze[a][b] == 3:
        global result
        result = 1
        return
    else:
        global visited
        visited[a][b] = True
        if b+1 <16 and maze[a][b+1] != 1 and visited[a][b+1] == False:
            dfs(a,b+1)
        if b>0 and maze[a][b-1] != 1 and visited[a][b-1] == False:
            dfs(a,b-1)
        if a+1< 16 and maze[a+1][b] != 1 and visited[a+1][b] == False:
            dfs(a+1,b)
        if a>0 and maze[a-1][b] != 1 and visited[a-1][b] == False:
            dfs(a-1,b)
        visited[a][b] = False


for test_case in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]
    result = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                dfs(i,j)
                break
    print('#{} {}'.format(tc, result))