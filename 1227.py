#1227. [S/W 문제해결 기본] 7일차 - 미로2
delta = [(1,0),(-1,0),(0,1),(0,-1)]

for test_case in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    visited = [[False for _ in range(100)] for _ in range(100)]
    result = 0
    stack = []
    for x in range(100):
        for y in range(100):
            if maze[x][y] == 2:
                stack.append((x,y))
    while stack:
        a,b = stack.pop()
        visited[a][b] = True
        if maze[a][b] ==3:
            result = 1
            break
        for dl in delta:
            dx = a + dl[0]
            dy = b + dl[1]
            if 0 < dx < 100 and 0 < dy < 100 and visited[dx][dy] == False and maze[dx][dy] != 1:
                stack.append((dx,dy))


    print('#{} {}'.format(tc, result))