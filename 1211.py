#1211

for test_case in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    dist_dict = {}
    min_val = 10000
    min_idx = 0
    for sp in range(100):
        if ladder[0][sp] ==1: #첫 행을 돌면서 1인 경우에만 시작!
            x = 0
            y = sp
            dist = 0
            while True:
                x += 1
                if x == 99:  #브레이크 조건 (나올 때)
                    break
                if y>0 and ladder[x][y-1] == 1:  #숫자조건이 앞에 붙는 이유는 0이 저 ladder[x][y-1] 조건을 만나자마자 에러가 뜨기 때몬입니다..
                    y -=1
                    dist +=1
                    while ladder[x+1][y] == 0:
                        y-=1
                        dist +=1
                elif y<99 and ladder[x][y+1] == 1:
                    y+=1 
                    dist +=1
                    while ladder[x+1][y] == 0:
                        y+=1
                        dist +=1
            dist_dict[sp] = dist
    for point, val in dist_dict.items():
        if val <= min_val:
            min_idx = point
            min_val = val
    print('#{} {}'.format(tc, min_idx))