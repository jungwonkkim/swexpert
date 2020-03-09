#5653. [모의 SW 역량테스트] 줄기세포배양
delta = [(0,1),(0,-1),(1,0),(-1,0)]

def incubate(time):
    global status
    global palette
    if time == K:
        return
    for a in range(K-time, K+N+time):
        for b in range(K-time, K+M+time):
            if status[a][b][0] == 0 or status[a][b] == [1,-1]:
                continue
            if status[a][b][0] == 1 and status[a][b][1] != -1:
                status[a][b][1] += 1
                if status[a][b][1] == palette[a][b]:
                    status[a][b] = [2,0]
                continue
            if status[a][b] == [2,0]:
                for dl in delta:
                    newa = a + dl[0]
                    newb = b + dl[1]
                    if status[newa][newb] == [1,-1] or status[newa][newb] == [0,0]:
                        if palette[newa][newb] < palette[a][b]:
                            palette[newa][newb] = palette[a][b]
                            status[newa][newb] = [1,-1]
                status[a][b][1] +=1
                if status[a][b][1] >= palette[a][b]:
                    status[a][b] = [0,-1]
                continue
            else:
                status[a][b][1] +=1
                if status[a][b][1] >= palette[a][b]:
                    status[a][b] = [0,-1]
                continue

    for a in range(K-time-1, K+N+time+1):
        for b in range(K-time-1, K+M+time+1):
            if status[a][b] == [1,-1]:
                status[a][b][1] +=1

    incubate(time+1)



T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    #status[0] 0 : 죽음 1: 비활성화 2:활성화 [1]: [0]이 0인경우 0:무존재 -1:죽음 나머지: 타임ㅁ
    status = [[[0,0] for _ in range(M+K*2)] for _ in range(N+K*2)]
    palette =[[0 for _ in range(M+K*2)] for _ in range(K)] + [[0]*K + list(map(int, input().split())) + [0]*K for _ in range(N)] + [[0 for _ in range(M+K*2)] for _ in range(K)]
    for i in range(K, K+N):
        for j in range(K, K+M):
            if palette[i][j]:
                status[i][j] = [1,0]
    incubate(0)
    cnt = 0
    for i in range(N+K*2):
        for j in range(M+K*2):
            if status[i][j][0]>0:
                cnt +=1
    print('#{} {}'.format(test_case, cnt))
