#백준 14500 테트로미노
delta = [(0,1),(0,-1),(1,0),(-1,0)]
def dfs(arr, cnt, idx):
    global max_cnt
    if idx == 4:
        if max_cnt < cnt:
            max_cnt = cnt
        return
    for dl in delta:
        for i in range(len(arr)):
            newx = arr[i][0] + dl[0]
            newy = arr[i][1] + dl[1]
            if 0<=newx<N and 0<=newy<M and (newx, newy) not in arr and visited[newx][newy] == False:
                arr.append((newx, newy))
                dfs(arr, cnt+board[newx][newy], idx+1)
                arr.pop()






N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
max_cnt = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs([(i,j)], board[i][j], 1)

print(max_cnt)