"""
백준 17142 연구소3
https://www.acmicpc.net/problem/17142
code written by jungwonkkim
"""
from itertools import combinations
from copy import deepcopy
delta = [(0,1),(1,0),(-1,0),(0,-1)]

def Verbreitung(arr, viruses):
    temp = deepcopy(arr)
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for virus in viruses:
        temp[virus[0]][virus[1]] = cnt
    queue = viruses
    while queue:
        cnt +=1
        blank = []
        deactivated = []
        for a, b in queue:
            for dl in delta:
                newa = a + dl[0]
                newb = b + dl[1]
                if -1 < newa < N and -1 < newb < N:
                    if temp[newa][newb] == -1:
                        temp[newa][newb] = cnt
                        blank.append((newa, newb))
                    elif temp[newa][newb] == '*' and visited[newa][newb] == False:
                        visited[newa][newb] = True
                        deactivated.append((newa, newb))
        queue = blank + deactivated
    for i in range(N):
        for j in range(N):
            if temp[i][j] == -1:
                return -1
    if blank:
        return cnt
    else:
        return cnt - 1

N, M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]
virus = []
min_time = 10000
for i in range(N):
    for j in range(N):
        if laboratory[i][j] == 0:
            laboratory[i][j] = -1
        elif laboratory[i][j] == 1:
            laboratory[i][j] = '-'
        else:
            virus.append((i,j))
            laboratory[i][j] = '*'
if virus:
    candidates = list(map(list, combinations(virus,M)))
    for candidate in candidates:
        time = Verbreitung(laboratory, candidate)
        if time == -1:
            continue
        if min_time > time:
            min_time = time
    if min_time == 10000:
        print(-1)
    else:
        print(min_time)
else:
    print(0)


