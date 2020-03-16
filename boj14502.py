#백준 14502 연구소
delta = [(0,1),(0,-1),(1,0),(-1,0)]
def simulation(n1, n2, n3):
    sim_lab = [[lab[i][j] for j in range(M)] for i in range(N)]
    sim_lab[n1[0]][n1[1]] = sim_lab[n2[0]][n2[1]] = sim_lab[n3[0]][n3[1]] = 1
    visited = [[False for _ in range(M)] for _ in range(N)]
    stack = []
    for x in range(N):
        for y in range(M):
            if sim_lab[x][y] == 2 and visited[x][y] == False:
                stack.append((x,y))
                while stack:
                    dx, dy = stack.pop()
                    visited[dx][dy] = True
                    for dl in delta:
                        nx = dx+dl[0]
                        ny = dy+dl[1]
                        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == False and sim_lab[nx][ny] == 0:
                            stack.append((nx,ny))
                            sim_lab[nx][ny] = 2
    cnt = 0
    for x in range(N):
        for y in range(M):
            if sim_lab[x][y] == 0:
                cnt +=1
    return cnt





N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
vacancy = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            vacancy.append((i,j))
max_area = 0
for a in range(len(vacancy)-2):
    for b in range(a+1, len(vacancy)-1):
        for c in range(b+1, len(vacancy)):
            if max_area < simulation(vacancy[a], vacancy[b], vacancy[c]):
                max_area = simulation(vacancy[a], vacancy[b], vacancy[c])
print(max_area)
