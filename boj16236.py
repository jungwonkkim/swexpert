"""
백준 16236 아기상어
https://www.acmicpc.net/problem/16236
Code written by jungwonkkim
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
가장 처음에 아기 상어의 크기는 2
"""
from copy import deepcopy

delta = [(-1,0),(0,-1), (0,1),(1,0)]

def fishfinder(x, y):
    global ate
    global shark
    global fishes
    global time
    global a
    global b
    dist = 1
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    queue = [(x,y)]
    while queue:
        new_queue = []
        flag = False
        minx = 20
        miny = 20
        for x, y in queue:
            for dl in delta:
                newx = x + dl[0]
                newy = y + dl[1]
                if -1 < newx < N and -1 < newy <N and visited[newx][newy] == False and fishes[newx][newy] <= shark:
                    visited[newx][newy] = True
                    new_queue.append((newx, newy))
                    if 0 < fishes[newx][newy] < shark:
                        flag = True
                        if minx > newx:
                            minx = newx
                            miny = newy
                        elif minx == newx:
                            if miny > newy:
                                miny = newy
        if flag:
            fishes[minx][miny] = 0
            a, b = minx, miny
            time += dist
            ate +=1
            if shark == ate:
                shark +=1
                ate = 0
            return True
        queue = deepcopy(new_queue)
        dist +=1
    return False


N = int(input())
fishes = [list(map(int, input().split())) for _ in range(N)]
shark = 2
ate = 0
time = 0
for i in range(N):
    for j in range(N):
        if fishes[i][j] == 9:
            a,b = i, j
            fishes[i][j] = 0
            break
while True:
    if fishfinder(a, b):
        continue
    else:
        break
print(time)