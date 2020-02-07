def up(arr):
    up_board = [[0 for _ in range(N)] for _ in range(N)]
    for upa in range(N):
        for upb in range(N):
            up_board[upa][upb] = arr[upb][N-1-upa]
    up_board = turn(up_board)
    nup_board = [[0 for _ in range(N)] for _ in range(N)]
    for upa in range(N):
        for upb in range(N):
            nup_board[upa][upb] = up_board[N-1-upb][upa]
    return nup_board

def down(arr):
    down_board = [[0 for _ in range(N)] for _ in range(N)]
    for downa in range(N):
        for downb in range(N):
            down_board[downa][downb] = arr[N-1-downb][downa]
    down_board = turn(down_board)
    ndown_board = [[0 for _ in range(N)]for _ in range(N)]
    for downa in range(N):
        for downb in range(N):
            ndown_board[downa][downb] = down_board[downb][N-1-downa]
    return ndown_board


def right(arr):
    right_board = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for rr in range(N):
            right_board[r][rr] = arr[r][rr]
        right_board[r].reverse()
    right_board = turn(right_board)
    for rrr in range(N):
        right_board[rrr].reverse()
    return right_board



def turn(arr1):
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    while True:
        for i in range(N):
            for j in range(N):
                new_board[i][j] = arr1[i][j]
        for i in range(N):
            for j in range(N):
                if arr1[i][j] == 0:
                    for k in range(j, N - 1):
                        arr1[i][k] = arr1[i][k+1]
                    arr1[i][N-1] = 0
        if arr1 == new_board:
            break
    for i in range(N):
        for j in range(N-1):
            if new_board[i][j] == 0 :
                break
            elif new_board[i][j] == new_board[i][j+1]:
                new_board[i][j] = new_board[i][j]*2
                for k in range(j+1, N-1):
                    new_board[i][k] = new_board[i][k+1]
                new_board[i][N-1] = 0
    return new_board



T = int(input())

for test_case in range(1, T + 1):
    N, cmd = input().split()
    N = int(N)
    game_board = [list(map(int, input().split())) for _ in range(N)]
    if cmd == 'left':
        game_board = turn(game_board)
    elif cmd =='up':
        game_board = up(game_board)
    elif cmd =='right':
        game_board = right(game_board)
    else:
        game_board = down(game_board)
    print('#{}'.format(test_case))
    for line in game_board:
        for res in line:
            print(res, end = ' ')
        print()