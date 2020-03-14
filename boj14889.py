#백준 14889 스타트와 링크

def energy(arr):
    cnt = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            cnt += synergy[arr[i]][arr[j]] + synergy[arr[j]][arr[i]]
    return cnt


def team_making(idx, team_A, team_B):
    global min_diff
    if idx == N:
        if min_diff > abs(energy(team_A) - energy(team_B)):
            min_diff = abs(energy(team_A) - energy(team_B))
        return
    if len(team_A) < N//2:
        team_A.append(idx)
        team_making(idx+1, team_A, team_B)
        team_A.pop()
    if len(team_B) < N//2:
        team_B.append(idx)
        team_making(idx+1, team_A, team_B)
        team_B.pop()





N = int(input())
synergy = [list(map(int, input().split())) for _ in range(N)]
min_diff= 100 * 400
team_making(1, [0], [])
print(min_diff)

