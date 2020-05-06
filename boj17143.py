"""
백준 17143 낚시왕
https://www.acmicpc.net/problem/17143
code written by jungwonkkim
s, d, z = 속력, 이동방향, 크기
"""
from copy import deepcopy
delta = [(0,0),(-1,0),(1,0),(0,1),(0,-1)]

R, C, M = map(int, input().split())
sea = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sea[r-1][c-1] = [s,d,z]
caught = 0
for c in range(C):
    new_sea = [[[] for _ in range(C)] for _ in range(R)]
    for r in range(R):
        if sea[r][c]:
            caught += sea[r][c][2]
            sea[r][c] = []
            break
    for i in range(R):
        for j in range(C):
            if sea[i][j]:
                newi = i + delta[sea[i][j][1]][0]*sea[i][j][0]
                newj = j + delta[sea[i][j][1]][1]*sea[i][j][0]
                while True: #바다 안으로 상어 넣기
                    if -1<newi<R and -1<newj<C:
                        break
                    if newi <0:
                        sea[i][j][1] = 2
                        newi = -newi
                    if newi >= R:
                        sea[i][j][1] = 1
                        newi = 2*R-newi-2
                    if newj <0:
                        sea[i][j][1] = 3
                        newj = -newj
                    if newj>= C:
                        sea[i][j][1] = 4
                        newj = 2*C-newj-2
                if new_sea[newi][newj]:
                    if new_sea[newi][newj][2]> sea[i][j][2]:
                        continue
                    else:
                        new_sea[newi][newj] = sea[i][j]
                else:
                    new_sea[newi][newj] = sea[i][j]
    sea = deepcopy(new_sea)
print(caught)

