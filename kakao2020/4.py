delta = [(1,0),(0,1), (-1,0),(0,-1)]
min_val = 1000001
N = 25
visited = []
roads = []

def dfs(i, j, cost, dir):
    global visited
    global min_val
    if i == j == N - 1:
        if min_val > cost:
            min_val = cost
        return
    if cost > min_val:
        return
    for idx in range(4):
        newi = i + delta[idx][0]
        newj = j + delta[idx][1]
        if -1 < newi < N and -1 < newj < N and roads[newi][newj] == 0 and visited[newi][newj] == False:
            visited[newi][newj] = True
            if i == j == 0 or idx == dir:
                dfs(newi, newj, cost + 100, idx)
            else:
                dfs(newi, newj, cost + 600, idx)
            visited[newi][newj] = False

def solution(board):
    global min_val
    global N
    global visited
    global roads
    roads = board
    N = len(board)
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[0][0] = True
    min_val = 500 * N * N
    dfs(0, 0, 0, 0)
    answer = min_val
    return answer

roads = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(roads))