#4012. [모의 SW 역량테스트] 요리사

def making(idx, team_A, team_B):
    global min_diff
    if idx == N:
        acnt = 0
        bcnt = 0
        for aidx in range(N//2):
            for aaidx in range(aidx+1, N//2):
                acnt += synergy[team_A[aidx]][team_A[aaidx]] + synergy[team_A[aaidx]][team_A[aidx]]
                bcnt += synergy[team_B[aidx]][team_B[aaidx]] + synergy[team_B[aaidx]][team_B[aidx]]
        if min_diff > abs(acnt - bcnt):
            min_diff = abs(acnt-bcnt)
        return
    if len(team_A)<N//2:
        team_A.append(idx)
        making(idx+1, team_A, team_B)
        team_A.pop()
    if len(team_B)<N//2:
        team_B.append(idx)
        making(idx+1, team_A, team_B)
        team_B.pop()


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    min_diff = 20000*256
    making(1, [0], [])
    print('#{} {}'.format(test_case, min_diff))
