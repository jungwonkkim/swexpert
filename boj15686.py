#백준 15686 치킨배달
#Code created by jungwonkkim

from itertools import combinations

N, M = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(N)]
house = []
kfc = []
for i in range(N):
    for j in range(N):
        if village[i][j] == 1:
            house.append((i, j))
        elif village[i][j] == 2:
            kfc.append((i, j))

distance = [[0 for _ in range(len(kfc))] for _ in range(len(house))]
for i in range(len(house)):
    for j in range(len(kfc)):
        distance[i][j] = abs(house[i][0]-kfc[j][0]) + abs(house[i][1]-kfc[j][1])

if M == len(kfc):
    cnt = 0
    for i in range(len(house)):
        cnt += min(distance[i])
    print(cnt)
else:
    min_dist = 100 * len(house)
    c = len(kfc) - M
    closing = list(combinations([n for n in range(len(kfc))], c))
    for closed in closing:
        cnt = 0
        for i in range(len(house)):
            new_list = [distance[i][j] for j in range(len(kfc)) if j not in closed]
            cnt += min(new_list)
            if min_dist < cnt:
                cnt = 100*len(house)
                break
        if min_dist > cnt:
            min_dist = cnt
    print(min_dist)