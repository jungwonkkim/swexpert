"""
백준 15684 사다리조작 python
https://www.acmicpc.net/problem/15684
Code by jungwonkkim
"""

def down(arr):
    global ladder
    for (nx, ny) in arr:
        ladder[nx][ny] = 1
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
            for (nx, ny) in arr:
                ladder[nx][ny] = 0
            return False
    return True


def dfs(chance, new_line):
    global min_val
    if min_val != -1: #이미 답 나왔을경우 더이상의 탐색 의미 없음
        return
    if chance == 0: #더이상 넣을 수 있는 기회가 없을 경우
        if down(new_line): #사다리 내리는 함수 진행후 만약 모든 i 번째 세로줄의 결승점이 i번째 일 경우
            min_val = cnt #min_val 값 cnt 로 고쳐준 후 함수 리턴
        return
    x, y = 0, 0
    if new_line:
        x, y = new_line[-1]
    for a in range(x, H):
        for b in range(N-1):
            if a == x and b <= y: #이전에 탐색 완료
                continue
            if b>0 and ladder[a][b-1]: #왼쪽에 선이 있는 경우
                continue
            if ladder[a][b]: #해당 장소에 선이 있는 경우
                continue
            if ladder[a][b+1]: #오른쪽에 선이 있는 경우
                continue
            new_line.append((a,b))
            dfs(chance-1, new_line)
            new_line.pop()


N, M, H = map(int, input().split())
ladder = [[0 for _ in range(N)] for _ in range(H)] #가로 N이고 세로 H인 사다리 만들기
min_val = -1
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1 #ladder[x][y] 가 1이라면 y번째와 y+1번째의 세로선이 x+1번째 가로선에서 이어져 있다는 뜻
for cnt in range(4):
    dfs(cnt, []) #cnt: 새로운 라인의 개수, 백트래킹을 위한 x,y좌표
    if min_val == -1: #그 전에서 아직 답이 나오지 않은 경우는 가능한 라인 개수를 늘린다.
        continue
    else:
        break
print(min_val)
