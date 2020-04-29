delta = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

def dfs(a,b):
    global visited
    stack = [(a,b)]
    while stack:
        x, y = stack.pop()
        visited[x][y] = True
        for dl in delta:
            nx = x + dl[0]
            ny = y + dl[1]
            if -1<nx<10 and -1<ny<10 and sky[nx][ny] and visited[nx][ny] == False and (nx,ny) not in stack:
                stack.append((nx, ny))

T = int(input())
for test_case in range(1, T+1):
    sky = [list(map(int, input().split())) for _ in range(10)]
    visited = [[False for _ in range(10)] for _ in range(10)]
    ans = 0
    for i in range(10):
        for j in range(10):
            if sky[i][j] and visited[i][j]== False:
                ans +=1
                dfs(i,j)
    print('#{} {}'.format(test_case, ans))
