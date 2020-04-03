#백준 게리맨더링 2

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
for x in range(1, N-1):
    for y in range(1, N-1):
        for d1 in range(2, min(x, y)):
            for d2(2, n-)