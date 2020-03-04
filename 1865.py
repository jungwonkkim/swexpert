#1865. 동철이의 일 분배

def dfs(idx, per):
    global max_per
    global visited
    if per < max_per:
        return
    if idx == N:
        max_per = per
        return
    for i in range(N):
        if visited[i]== False:
            visited[i] = True
            dfs(idx+1, per * workspace[idx][i]/100)
            visited[i] = False


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    workspace = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    max_per = 0
    dfs(0,1)
    max_per *= 100
    print("#{} {:.6f}".format(test_case, max_per))