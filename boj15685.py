#백준 15685 드래곤 커브
#Code created by jungwonkkim

delta = [(1,0),(0,-1),(-1,0),(0,1)]

N = int(input())
d_curve = [[0 for _ in range(101)] for _ in range(101)]
for n in range(N):
    x, y, d, g = map(int, input().split())
    dragon = [(x, y)]
    dragon.append((x+delta[d][0], y+delta[d][1]))
    cnt = 0
    next_end = 1
    while cnt < g:
        end = next_end
        new_dragon = []
        for i in range(len(dragon)):
            if i == end:
                continue
            nx = dragon[i][0] - dragon[end][0]
            ny = dragon[i][1] - dragon[end][1]
            new_dragon.append((dragon[end][0] - ny,  dragon[end][1] + nx))
        next_end = len(dragon)
        dragon.extend(new_dragon)
        cnt +=1
    for dr in dragon:
        d_curve[dr[0]][dr[1]] = 1
cnt = 0
for a in range(100):
    for b in range(100):
        if 1 == d_curve[a][b] == d_curve[a][b+1] == d_curve[a+1][b] == d_curve[a+1][b+1]:
                cnt += 1
print(cnt)