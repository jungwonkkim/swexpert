#1953. [모의 SW 역량테스트] 탈주범 검거

upper = [1,2,5,6]
under = [1,2,4,7]
left = [1,3,4,5]
right = [1,3,6,7]

def one(x,y):
    if x-1>=0 and route[x-1][y] in upper and visited[x-1][y] == False:
        result.append((x-1,y))
    if x+1<N and route[x+1][y] in under and visited[x+1][y] == False:
        result.append((x+1, y))
    if y-1>=0 and route[x][y-1] in left and visited[x][y-1] == False:
        result.append((x,y-1))
    if y+1<M and route[x][y+1] in right and visited[x][y+1] == False:
        result.append((x,y+1))
def two(x,y):
    if x-1>=0 and route[x-1][y] in upper and visited[x-1][y] == False:
        result.append((x-1,y))
    if x+1<N and route[x+1][y] in under and visited[x+1][y] == False:
        result.append((x+1, y))
def three(x,y):
    if y-1>=0 and route[x][y-1] in left and visited[x][y-1] == False:
        result.append((x,y-1))
    if y+1<M and route[x][y+1] in right and visited[x][y+1] == False:
        result.append((x,y+1))
def four(x,y):
    if x-1>=0 and route[x-1][y] in upper and visited[x-1][y] == False:
        result.append((x-1,y))
    if y+1<M and route[x][y+1] in right and visited[x][y+1] == False:
        result.append((x,y+1))
def five(x,y):
    if x+1<N and route[x+1][y] in under and visited[x+1][y] == False:
        result.append((x+1, y))
    if y+1<M and route[x][y+1] in right and visited[x][y+1] == False:
        result.append((x,y+1))
def six(x,y):
    if x+1<N and route[x+1][y] in under and visited[x+1][y] == False:
        result.append((x+1, y))
    if y-1>=0 and route[x][y-1] in left and visited[x][y-1] == False:
        result.append((x,y-1))
def seven(x,y):
    if x-1>=0 and route[x-1][y] in upper and visited[x-1][y] == False:
        result.append((x-1,y))
    if y-1>=0 and route[x][y-1] in left and visited[x][y-1] == False:
        result.append((x,y-1))


def bfs(time):
    global result
    result = []
    if time > 0:
        for a in range(N):
            for b in range(M):
                if visited[a][b] and a + b > L-time:
                    if route[a][b] == 1:
                        one(a,b)
                    if route[a][b] ==2:
                        two(a,b)
                    if route[a][b] ==3:
                        three(a,b)
                    if route [a][b] == 4:
                        four(a,b)
                    if route[a][b] == 5:
                        five(a,b)
                    if route[a][b] == 6:
                        six(a,b)
                    if route[a][b] == 7:
                        seven(a,b)
        for res in result:
            visited[res[0]][res[1]] = True
        bfs(time-1)




T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    route = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[R][C] = True
    counter = 0
    bfs(L-1)
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                counter +=1
    print('#{} {}'.format(test_case, counter))
