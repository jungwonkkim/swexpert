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


T = int(input())

for test_case in range(1, T+1):
    N, B = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]
    if B == 'up':
        board = up(board)
    elif B == 'down':
        board = down(board)
    elif B == 'right':
        board = right(board)
    else:
        board = turn(board)
    print('#{}'.format(test_case))
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = ' ')
        print()
