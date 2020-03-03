#2819. 격자판의 숫자 이어 붙이기
delta = [(1,0),(-1,0),(0,1),(0,-1)]

def search(arr, cnt):
    global result
    if cnt == 7:
        while arr:
            res = arr.pop()[2]
            result.add(res)
        return
    else:
        newarr = []
        while arr:
            a, b , ans = arr.pop()
            for dl in delta:
                nx = a+dl[0]
                ny = b+dl[1]
                if -1<nx<4 and -1<ny<4:
                    newarr.append((nx, ny, ans+str(board[nx][ny])))
        search(newarr, cnt+1)



T = int(input())

for test_case in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            search([(i, j, str(board[i][j]))], 1)
    print('#{} {}'.format(test_case, len(result)))