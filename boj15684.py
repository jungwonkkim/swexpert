"""
백준 15684 사다리조작 python
https://www.acmicpc.net/problem/15684
Code by jungwonkkim
"""

def down(): #사다리 조건 확인 함수
    for i in range(N):
        s = i
        j = 0
        while j < H:
            if ladder[j][s]:
                s += 1
                j += 1
            elif s > 0 and ladder[j][s-1]:
                s -= 1
                j += 1
            else:
                j += 1
        if s == i:
            continue
        else:
            return False
    return True


def dfs(chance, x, y):
    global min_val
    global ladder
    if min_val != -1: #이미 답 나왔을경우 더이상의 탐색 의미 없음
        return
    if chance == 0: #더이상 넣을 수 있는 기회가 없을 경우
        if down(): #사다리 내리는 함수 진행후 만약 모든 i 번째 세로줄의 결승점이 i번째 일 경우
            min_val = cnt #min_val 값 cnt 로 고쳐준 후 함수 리턴
        return
    for dx in range(x, H):
        for dy in range(N-1):
            if dx == x and dy <= y: #이전에 탐색 완료
                continue
            if dy > 0 and ladder[dx][dy-1]: #왼쪽에 선이 있는 경우
                continue
            if ladder[dx][dy] or ladder[dx][dy+1]: #해당 장소 혹은 오른쪽에 선이 있는 경우
                continue
            ladder[dx][dy] = 1
            dfs(chance-1, dx, dy)
            ladder[dx][dy] = 0


N, M, H = map(int, input().split())
ladder = [[0 for _ in range(N)] for _ in range(H)] #가로 N이고 세로 H인 사다리 만들기
min_val = -1
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1 #ladder[x][y] 가 1이라면 y번째와 y+1번째의 세로선이 x+1번째 가로선에서 이어져 있다는 뜻
for cnt in range(4):
    dfs(cnt, 0, -1) #cnt: 새로운 라인의 개수, 백트래킹을 위한 x,y좌표
    if min_val == -1: #그 전에서 아직 답이 나오지 않은 경우는 가능한 라인 개수를 늘린다.
        continue
    else:
        break
print(min_val)
