#백준 505대회 2번 - Gaaarden
#code created by jungwonkkim
from itertools import combinations
import copy

delta = [(0,1), (0,-1), (1,0), (-1,0)]

def water_divide(idx, r, g):
    global max_fcnt
    if idx == R+G:
        watered = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if garden[i][j] == 0:
                    watered[i][j] = -1
        old_r = r
        old_g = g
        while True:
            new_r = []
            new_g = []
            for ele in old_r:
                watered[ele[0]][ele[1]] = 2
                for dl in delta:
                    nx = ele[0] + dl[0]
                    ny = ele[1] + dl[1]
                    if -1 < nx < N and -1 < ny < M and watered[nx][ny] == 0 and (nx,ny) not in new_r and (nx,ny) not in old_r:
                        new_r.append((nx, ny))
            for ele in old_g:
                watered[ele[0]][ele[1]] = 1
                for dl in delta:
                    nx = ele[0] + dl[0]
                    ny = ele[1] + dl[1]
                    if -1 < nx < N and -1 < ny < M and watered[nx][ny] == 0 and (nx,ny) not in new_g and (nx,ny) not in old_g:
                        new_g.append((nx, ny))
            if new_r == [] and new_g == []:
                break
            flower = []
            for ele in new_r:
                if ele in new_g:
                    flower.append(ele)
                    watered[ele[0]][ele[1]] = 3
            for f in flower:
                new_r.remove(f)
                new_g.remove(f)
            old_r = copy.deepcopy(new_r)
            old_g = copy.deepcopy(new_g)
        fcnt = 0
        for i in range(N):
            for j in range(M):
                if watered[i][j] == 3:
                    fcnt += 1
        if max_fcnt < fcnt:
            max_fcnt = fcnt
        return
    if len(r) < R:
        r.append(w[idx])
        water_divide(idx+1, r, g)
        r.pop()
    if len(g) < G:
        g.append(w[idx])
        water_divide(idx+1, r, g)
        g.pop()



N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
waterable = []
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            waterable.append((i, j))
max_fcnt = 0
water = list(map(list, combinations(waterable, R+G)))
for w in water:
    if R == G:
        water_divide(1, [w[0]], [])
    else:
        water_divide(0, [], [])
print(max_fcnt)
