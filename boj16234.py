delta = [(0,1),(1,0),(-1,0),(0,-1)]


def dfs(x,y):
    global visited
    global flag
    stack = [(x,y)]
    queue = [(x,y)]
    population = countries[x][y]
    for dl in delta:
        nx = x + dl[0]
        ny = y + dl[1]
        if -1<nx<N and -1<ny<N and visited[nx][ny] == False and L <= abs(countries[x][y] - countries[nx][ny]) <=R:
            population += countries[nx][ny]
            stack.append((nx,ny))
            queue.append((nx,ny))
            flag = True
    if flag:
        while stack:
            a, b = stack.pop()
            for dl in delta:
                na = a + dl[0]
                nb = b + dl[1]
                if -1<na<N and -1<nb<N and visited[na][nb] == False and (na,nb) not in queue and L<= abs(countries[a][b] - countries[na][nb])<=R:
                    population += countries[na][nb]
                    stack.append((na, nb))
                    queue.append((na,nb))
        new = population // len(queue)
        for q in queue:
            visited[q[0]][q[1]] = True
            countries[q[0]][q[1]] = new
        return
    else:
        visited[x][y] = True
        return

N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]
move = 0
while True:
    flag = False
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                dfs(i,j)
    if flag:
        move +=1
        continue
    else:
        break

print(move)