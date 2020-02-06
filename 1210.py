#1210. [S/W 문제해결 기본] 2일차 - Ladder1


for test_case in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    for sp in range(100):
        if ladder[0][sp] ==1: #첫 행을 돌면서 1인 경우에만 시작!
            x = 0
            y = sp
            while True:
                x += 1
                if x == 99:  #브레이크 조건 (나올 때)
                    break
                if y>0 and ladder[x][y-1] == 1:  #숫자조건이 앞에 붙는 이유는 0이 저 ladder[x][y-1] 조건을 만나자마자 에러가 뜨기 때몬입니다..
                    y -=1
                    while ladder[x+1][y] == 0:
                        y-=1
                elif y<99 and ladder[x][y+1] == 1:
                    y+=1 
                    while ladder[x+1][y] == 0:
                        y+=1
            if ladder[99][y] ==2:
                result = sp
                break
        
    print('#{} {}'.format(tc, result)