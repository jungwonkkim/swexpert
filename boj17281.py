"""
code by jungwonkkim
https://www.acmicpc.net/problem/17281
백준 야구
"""

import itertools

pool = [1,2,3,4,5,6,7,8]
combination = itertools.permutations(pool)

def play(player):
    inning = N
    h = 0
    i = 0
    out_counter = 0
    point = 0
    field = [0,0,0,0]
    while inning>0:
        hit = player[i][h]
        if hit == 0:
            out_counter +=1
        if out_counter == 3:
            field = [0,0,0,0]
            inning -=1
            h = +1
            out_counter = 0
        if hit ==1:
            for j in range(2,0,-1):
                field[j] = field[j-1]
            field[0] = 1
            if field[3] ==1:
                point +=1
            field[3] = 0
        if hit == 2:
            for k in range(1, 3):
                if field[k] ==1:
                    point+=1
                    field[k] = 0
            field[2] = field[0]
            field[0] = 0
            field[1] = 1
        if hit == 3:
            for l in field:
                if l ==1 :
                    point+=1
            field = [1,0,0,0]
        if hit == 4:
            point+=1
            for m in field:
                if m == 1:
                    point+=1
            field = [0,0,0,0]
        i +=1
        if i == 9:
            i = 0
    return point


N = int(input())
temp_list = [list(map(int, input().split())) for _ in range(N)]
playerz = [[0 for _ in range(N)] for _ in range(9)]
pointzz = 0
for b in range(9):
    for c in range(N):
        playerz[b][c] = temp_list[c][b]
for combi in combination:
    playert = [playerz[combi[d]] for d in range(8)]
    playert.insert(4,playerz[0])
    if play(playert) > pointzz:
        pointzz = play(playert)
print(pointzz)