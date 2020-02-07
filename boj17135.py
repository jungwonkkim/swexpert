def killing (x, y, bound):
    for i in range(-bound+1, bound):
        newx = bound - abs(i)
        newy = i
        if x-newx >-1 and  x-newx< N and y+newy > -1 and y+newy < M:
            if (x-newx,y+newy) not in deadmen and field[x-newx][y+newy] == 1:
                return (x-newx, y+newy)
    else:
        return None

def attack (combination):
    global deadmen
    archery = [combination[0], combination[1], combination[2]]
    dist = combination[3]
    deadmen = []
    E = len(field)-1
    for turn in range(N):
        enemy_point = []
        if field[:E] == 0:
            break
        for arch in archery:
            for num in range(1, dist+1):
                if killing(E, arch, num):
                    enemy_point.append(killing(E, arch, num))
                    break
        E -= 1
        enemy_point = list(set(enemy_point))
        deadmen.extend(enemy_point)
    enemy = len(deadmen)
    return enemy


N, M, D = map(int, input().split())
field = [[] for _ in range(N+1)]
max_kill = 0
arch_combi = []
for i in range(N):
    field[i] = list(map(int, input().split()))

for arch1 in range(M-2):
    for arch2 in range(arch1+1, M-1):
        for arch3 in range(arch2+1, M):
            arch_combi.append((arch1, arch2, arch3, D))

for chance in arch_combi:
    kill = attack(chance)
    if kill > max_kill:
        max_kill = kill

print(max_kill)