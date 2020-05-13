"""
백준 17142 연구소3
https://www.acmicpc.net/problem/17142
code written by jungwonkkim
"""
from copy import deepcopy
from itertools import combinations

delta = [(0,1),(1,0),(-1,0),(0,-1)]

def Verbreitung(arr, viruses):
    temp = deepcopy(arr)
    cnt = -1
    queue = viruses
    visited = [[False for _ in range(N)] for _ in range(N)]
    for v in viruses:
        visited[v[0]][v[1]] = True
    while queue:
        cnt +=1
        new_queue = []
        for a, b in queue:
            temp[a][b] = cnt
            for dl in delta:
                newa = a + dl[0]
                newb = b + dl[1]
                if -1 < newa < N and -1 < newb < N and visited[newa][newb] == False:
                    if temp[newa][newb] == -1 or temp[newa][newb] == '*':
                        visited[newa][newb] = True
                        new_queue.append((newa,newb))
        queue = deepcopy(new_queue)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '-1':
                return -1
    return cnt

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
candidates = list(map(list, combinations(virus,M)))
for candidate in candidates:
    time = Verbreitung(laboratory, candidate)
    if time == -1:
        continue
    else:
        if min_time > time:
            min_time = time
if min_time == 10000:
    print(-1)
else:
    print(min_time)



