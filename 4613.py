#4613. 러시아 국기 같은 깃발
def white(idx):
    paint = 0
    for a in range(idx+1):
        for b in range(M):
            if flag[a][b] != 'W':
                paint += 1
    if min_val > paint:
        for c in range(idx+1, N-1):
            blue(idx+1, c, paint)

def blue(sp, en, cnt):
    paint = cnt
    global min_val
    for a in range(sp, en+1):
        for b in range(M):
            if flag[a][b] != 'B':
                paint+=1
    if min_val > paint:
        for a in range(en+1, N):
            for b in range(M):
                if flag[a][b] != 'R':
                    paint+=1
        if min_val > paint:
            min_val = paint




T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    min_val = N * M
    for i in range(N-2):
        white(i)
    print('#{} {}'.format(test_case, min_val))