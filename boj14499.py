#백준 주사위 굴리기

def move(num, arr): #이동 함수
    if num == 1: #동
        arr[1], arr[3], arr[6], arr[4]= arr[4], arr[1], arr[3], arr[6]
    elif num == 2: #서
        arr[1], arr[3], arr[6], arr[4] = arr[3], arr[6], arr[4], arr[1]
    elif num == 3: #북
        arr[1], arr[5], arr[6], arr[2] = arr[5], arr[6], arr[2], arr[1]
    else: #남
        arr[1], arr[5], arr[6], arr[2] = arr[2], arr[1], arr[5], arr[6]
    print(arr[1]) #이동 가능한 경우에만 애초에 이 함수 안에 들어오기 때문에 이 함수 안에서 맨 위면의 값 출력해줌
    return arr

delta = [(0,0),(0,1), (0,-1), (-1,0),(1,0)]
N, M, x, y, K = map(int, input().split())
dice = [0,0,0,0,0,0,0]
maps = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
for cmd in command:
    if -1< x + delta[cmd][0] <N and -1 < y + delta[cmd][1] < M: #이동이 가능한지!
        x = x + delta[cmd][0]
        y = y + delta[cmd][1]
        dice = move(cmd, dice)
        if maps[x][y]: #지도에 값이 있을 경우 주사위 값 바꿔주고 지도 값 0으로 바꾸기
            dice[6] = maps[x][y]
            maps[x][y] = 0
        else: #지도에 값이 0일 경우 주사위 값을 지도에 옮겨주기
            maps[x][y] = dice[6]
    else:
        continue
