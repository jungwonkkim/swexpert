delta =[(-1,0),(1,0),(0,-1),(0,1)]

def dust(arr):
    plus_list = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] >0:
                give = arr[i][j]//5
                for dl in range(4):
                    newx = delta[dl][0]
                    newy = delta[dl][1]
                    if j + newy == 0 and i+newx == air:
                        continue
                    elif j + newy == 0 and i+ newx == air+1:
                        continue
                    elif i + newx > -1 and i+newx < R and j+newy > -1 and j+newy < C:
                        plus_list[i+newx][j+newy]+=give
                        plus_list[i][j] -=give
    for sero in range(R):
        for garo in range(C):
            arr[sero][garo] += plus_list[sero][garo]
    return arr

def purifier(arr, upper):
    for a in range(upper-1, 0,-1):
        arr[a][0] = arr[a-1][0]
    for b in range(1, C):
        arr[0][b-1] = arr[0][b]
    for c in range(1, upper+1):
        arr[c-1][C-1] = arr[c][C-1]
    for d in range(C-1, 1, -1):
        arr[upper][d] = arr[upper][d-1]
    arr[upper][1] = 0
    lower = upper+1
    for e in range(lower+1, R-1):
        arr[e][0] = arr[e+1][0]
    for f in range(C-1):
        arr[R-1][f] = arr[R-1][f+1]
    for g in range(R-1, lower, -1):
        arr[g][C-1] = arr[g-1][C-1]
    for h in range(C-1, 1, -1):
        arr[lower][h] = arr[lower][h-1]
    arr[lower][1] = 0
    return arr

R , C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
left= 0
for search in range(R):
    if room[search][0] == -1:
        air = search
        break

while T>0:
    room = dust(room)
    room = purifier(room, air)
    T-=1
for y in range(R):
    for z in range(C):
        if room[y][z] > 0 :
            left+= room[y][z]
print(left)

