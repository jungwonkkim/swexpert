#1220. [S/W 문제해결 기본] 5일차 - Magnetic

for test_case in range(1,11):
    n = int(input())
    origin_mlist = [[0 for _ in range(100)] for _ in range(100)]
    turn_mlist = [[0 for _ in range(100)] for _ in range(100)]
    one_count = 0
    dl_count = 0
    for i in range(100):
        origin_mlist[i] = list(map(int, input().split()))
    for i in range(100):
        for j in range(100):
            turn_mlist[i][j] = origin_mlist[j][i]
    for i in range(100):
        one_count = 0
        for j in range(100):
            if turn_mlist[i][j] == 1:
                one_count = 1
            elif turn_mlist[i][j] ==2:
                if one_count == 1:
                    dl_count +=1
                    one_count = 0
    print(f'#{test_case} {dl_count}')