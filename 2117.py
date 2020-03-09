#2117. [모의 SW 역량테스트] 홈 방범 서비스
def housekeeping(x, y):
    global max_house
    if N % 2:
        for K in range(N,0,-1):
            cnt = 0
            for a in range(max(x-K+1,0), min(N, x+K)):
                for b in range(max(y-K+1,0),min(N,y+K)):
                    if abs(a-x) + abs(b-y) < K and village[a][b]:
                        cnt +=1
            if cnt > max_house and K*K + (K-1)**2 <= cnt * M:
                max_house = cnt
    else:
        for K in range(N+1,0,-1):
            cnt = 0
            for a in range(max(x-K+1,0), min(x+K, N)):
                for b in range(max(y-K+1,0), min(y+K, N)):
                    if abs(a-x) + abs(b-y)<K and village[a][b]:
                        cnt +=1
            if cnt > max_house and K*K + (K-1)**2 <=cnt* M:
                max_house = cnt



T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    village = [list(map(int, input().split())) for _ in range(N)]
    max_house  = 0
    for i in range(N):
        for j in range(N):
            housekeeping(i, j)
    print('#{} {}'.format(test_case, max_house))