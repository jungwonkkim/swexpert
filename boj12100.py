#백준12100. 2048
def turn(arr1):
    for i in range(N):
        for j in range(N-2,-1,-1):
            if arr1[i][j] == 0:
                for k in range(j, N - 1):
                    arr1[i][k] = arr1[i][k+1]
                arr1[i][N-1] = 0
    for i in range(N):
        for j in range(N-1):
            if arr1[i][j] == 0:
                break
            if arr1[i][j] == arr1[i][j+1]:
                arr1[i][j] *= 2
                if j < N-2:
                    for k in range(j+1, N-1):
                        arr1[i][k] = arr1[i][k+1]
                arr1[i][N-1] = 0
    return arr1

def rotate(arr2):
    up_board = [[0 for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            up_board[a][b] = arr2[b][N - 1 - a]
    return up_board

def up(arr3):
    return rotate(rotate(rotate(turn(rotate(arr3)))))

def right(arr5):
    return rotate(rotate(turn(rotate(rotate(arr5)))))

def down(arr4):
    return rotate(turn(rotate(rotate(rotate(arr4)))))

def bfs(count):
    global board_bfs
    global max_val
    if count == 5:
        while board_bfs:
            temp = board_bfs.pop()
            for i in range(N):
                for j in range(N):
                    max_val = max(max_val, temp[i][j])
        return
    if count < 5:
        new_board_bfs = []
        while board_bfs:
            temp = board_bfs.pop()
            new_board_bfs.append(up(temp))
            new_board_bfs.append(down(temp))
            new_board_bfs.append(turn(temp))
            new_board_bfs.append(right(temp))
        board_bfs = [i for i in new_board_bfs]
        bfs(count+1)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
board_bfs = [board]
max_val = 0
bfs(0)
print(max_val)
