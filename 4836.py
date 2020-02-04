#4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
#델타 리스트 생성 
T = int(input())

for test_case in range(1, T + 1):
    color_board = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1,x2+1): 
            for y in range(y1,y2+1):   #색칠되어있지 않거나, 이미 동일한 색깔로 색칠 되어있는 경우
                if color_board[x][y] == 0 or color_board[x][y] == color:
                    color_board[x][y] = color
                else: #다른 색깔로 색칠되어있는 경우에 보라색으로 색칠하기
                    color_board[x][y] =3
    three_counter = 0
    for i in range(10): #이차원 리스트 중 보라색인 부분의 개수 카운트
        three_counter += color_board[i].count(3)
    print(f'#{test_case} {three_counter}')
