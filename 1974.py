#1974. 스도쿠 검증

T = int(input())

for test_case in range(1, T + 1):
    garo_list = [list(map(int, input().split())) for _ in range(9)]
    sero_list = [[0 for _ in range(9)] for _ in range(9)]
    result = 1
    for i in range(9):
        if len(set(garo_list[i])) != 9 :
            result = 0
            break
    if result:
        for i in range(9):
            for j in range(9):
                sero_list[i][j] = garo_list[j][i]
            if len(set(sero_list[i])) != 9:
                result = 0
                break
    if result:
        b = 0
        while(b < 9):
            if result == 0:
                break
            a = 0
            while(a < 9):
                nemo_list = []
                for i in range(a, a+3):
                    for j in range(b,b+3):
                        nemo_list.append(garo_list[i][j])
                if len(set(nemo_list)) != 9:
                    result = 0
                    break
                a+=3
            b+=3

    print('#{} {}'.format(test_case, result))