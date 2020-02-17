#14503 로봇청소기
dl = [(-1,0),(0,1),(1,0),(0,-1)] #북 동 남 서
rotate = [(0,-1),(1,0),(0,1),(-1,0)] # 서 남 동 북 0 = 0부터 1 = 3부터 2 = 2부터 3 = 1부터

def clean(x, y, d):
    global cnt
    if visited[x][y] == False:
        cnt+=1
        visited[x][y] = True #1번.현재 위치를 청소한다.
    if d == 0 or d == 2: #왼쪽으로 돌기(북 ->서, 남->동)
        rd = d
    else: #(서->남, 동->북)
        rd = 4-d
    shift = 0
    while shift<4: #2번. 현재위치에서 현재 방향을 기준으로
        #왼쪽방향부터 차례대로 탐색을 진행한다.(rotate 함수 이용)
        dx = rotate[rd][0] #도는 방향의 델타
        dy = rotate[rd][1]
        if 0<x+dx<N-1 and 0<y+dy<M-1 and room[x+dx][y+dy] == 0 and visited[x+dx][y+dy] == False: #왼쪽방향이 벽이 아니고
            clean(x+dx,y+dy,3-rd) #방문한적 없다면 그 방향으로 가서 1번부터 진행하기
            return
        else:
            shift+=1
            rd += 1 #2(b). 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
            if rd == 4:
                rd = 0
    nx = dl[d][0] #2(c) 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는
    ny = dl[d][1]
    if 0<x-nx<N-1 and 0<y-ny<M-1 and room[x-nx][y-ny] == 0:
        clean(x-nx, y-ny, d)#바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
        return
    else: #2(d) 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동멈추기
        return

N, M = map(int, input().split()) #세로크기와 가로크기가 주어진다
r, c, direction = map(int, input().split()) #로봇청소기의 좌표와 방향 d
visited = [[False for _ in range(M)] for _ in range(N)]
room = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
clean(r,c,direction)
print(cnt)