def dfs(x,y,z):
    global max_count
    if x == N-1 and y == N-1:
            max_count += 1
    else:
        if z == 0:
            if y < N-1 and pipe_line[x+0][y+1] == 0:
                dfs(x,y+1,0)
            if y< N-1 and x<N-1 and pipe_line[x+0][y+1]==pipe_line[x+1][y+0] == pipe_line[x+1][y+1] == 0:
                dfs(x+1,y+1,2)
        if z == 1:
            if x < N-1 and pipe_line[x+1][y+0] == 0:
                dfs(x+1,y,1)
            if y< N-1 and x<N-1 and pipe_line[x+0][y+1]==pipe_line[x+1][y+0] == pipe_line[x+1][y+1] == 0:
                dfs(x+1,y+1,2)
        if z == 2:
            if x < N-1 and pipe_line[x+1][y+0] == 0:
                dfs(x+1,y,1)
            if y < N - 1 and pipe_line[x + 0][y + 1] == 0:
                dfs(x, y + 1, 0)
            if y< N-1 and x<N-1 and pipe_line[x+0][y+1]==pipe_line[x+1][y+0] == pipe_line[x+1][y+1] == 0:
                dfs(x+1,y+1,2)

N = int(input())
pipe_line = [list(map(int, input().split())) for _ in range(N)]
max_count = 0
dfs(0,1,0)
print(max_count)