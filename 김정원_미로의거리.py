from copy import deepcopy

delta = [(0,1), (0,-1), (1,0), (-1, 0)]

def bfs(a, b):
    global dist
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    queue = [(a, b)]
    while queue:
        new_queue = []
        for q in queue:
            visited[q[0]][q[1]] = True
            for dl in delta:
                nx = q[0] + dl[0]
                ny = q[1] + dl[1]
                if -1<nx<N and -1<ny<N and maze[nx][ny] == 3:
                    dist = cnt
                    return
                if -1<nx<N and -1<ny<N and maze[nx][ny]==0 and visited[nx][ny]== False:
                    new_queue.append((nx, ny))
        queue = deepcopy(new_queue)
        cnt +=1
    return


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    dist = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                bfs(i, j)
    print('#{} {}'.format(test_case, dist))