pipe = [(1,0),(0,1),(1,1)]

def dfs(x,y):
    global prev
    global max_count
    if x == N-1 and y == N-1 and route not in visited:
        visited.append(route)
        print(visited)
        max_count += 1
    else:
        for i in range(0,3):
            dx = pipe[i][0]
            dy = pipe[i][1]
            if x + dx == N or y + dy == N: #선 밖으로 넘어갈 때
                continue
            if pipe_line[x][y+dy] != 0 or pipe_line[x+dx][y] != 0 or pipe_line[x+dx][y+dy] != 0: #범위 내 벽이 있을 때
                continue
            if (dx,dy) == (1,0) and prev == (0,1): # 가로였을 때 세로로 가려고 할 때
                continue
            if (dx,dy) == (0,1) and prev == (1,0): #세로였을 때 가로로 가려고 할 때
                continue
            if x+dx == N-1 and y != N-1 and (dx,dy) == (1,0):
                continue
            if y+dy == N-1 and x != N-1 and (dx,dy) == (0,1):
                continue
            prev = (dx,dy)
            route.append((x+dx,y+dy))
            dfs(x+dx, y+dy)




N = int(input())
pipe_line = [list(map(int, input().split())) for _ in range(N)]
max_count = 0
visited = []
route = [(0,1)]
prev = (0,1)
dfs(0,1)
print(max_count)
