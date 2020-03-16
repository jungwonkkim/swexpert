#code created by jungwonkkim

#1210. [S/W 문제해결 기본] 2일차 - Ladder1
def ladderup(y):
        x = 99
        while True:
            x -= 1
            if x == 0:  #브레이크 조건 (나올 때)
                break
            if y>0 and ladder[x][y-1] == 1:
                y -=1
                while ladder[x-1][y] == 0:
                    y-=1
            elif y<99 and ladder[x][y-1] == 1:
                y+=1
                while ladder[x+1][y] == 0:
                    y+=1
        return y

for test_case in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladder[99][i] ==2:
            sp = i
            break
    result = ladderup(sp)
        
    print('#{} {}'.format(tc, result)