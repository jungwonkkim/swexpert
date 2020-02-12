#2382. [모의 SW 역량테스트] 미생물 격리
def move(arr):
    if arr[3] == 1:
        arr[0] = arr[0]-1
        if arr[0] == 0:
            arr[3] = 2
            arr[2] = arr[2]//2
    elif arr[3] == 2:
        arr[0] = arr[0]+1
        if arr[0] == N-1:
            arr[3] = 1
            arr[2] = arr[2]//2
    elif arr[3] == 3:
        arr[1] = arr[1]-1
        if arr[1] == 0:
            arr[3] = 4
            arr[2] = arr[2]//2
    elif arr[3] == 4:
        arr[1] = arr[1]+1
        if arr[1] == N-1:
            arr[3] = 3
            arr[2] = arr[2]//2
    return arr

def collide(x,y):
    collision = []
    delete = []
    for idx, micky in enumerate(micro):
        if micky[0] == x and micky[1] == y:
            collision.append(micky)
            delete.append(idx)
    new_m = [x,y,0,0]
    max_con = 0
    for c in collision:
        new_m[2]+= c[2]
        if c[2]> max_con:
            max_con = c[2]
            new_m[3] = c[3]
    for d in range(len(delete)-1, -1, -1):
        del micro[delete[d]]
    micro.append(new_m)



def bfs(time):
    print(micro)
    if time>0:
        quantity = [[0 for _ in range(N)] for _ in range(N)]
        for m in micro:
            m = move(m)
            quantity[m[0]][m[1]] +=1
        for i in range(N):
            for j in range(N):
                if quantity[i][j] > 1:
                    collide(i,j)
        bfs(time-1)




T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    micro = [list(map(int, input().split())) for _ in range(K)]
    bfs(M)
    counter = 0
    for mi in micro:
        counter += mi[2]
    print('#{} {}'.format(test_case, counter))