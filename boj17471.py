#17471. 게리맨더링
def final_link(arr):
    if len(arr) == 0:
        return False
    if len(arr) ==1:
        return True
    visited = [False for _ in range(N)]
    stack = [arr[0]]
    while stack:
        find = stack.pop()
        visited[find] = True
        for b in range(N):
            if b in arr and graph[find][b] and visited[b] == False:
                stack.append(b)
    for a in arr:
        if visited[a] == False:
            return False
    return True


def divider(idx, teamA, teamB):
    global res
    if idx == N and final_link(teamA) and final_link(teamB):
        pop_A = 0
        pop_B = 0
        for A in teamA:
            pop_A += population[A]
        for B in teamB:
            pop_B += population[B]
        diff = abs(pop_A - pop_B)
        if res> diff:
            res = diff
        return
    teamA.append(idx)
    divider(idx+1, teamA, teamB)
    teamA.pop()
    if teamA ==[] and teamB ==[]:
        return
    teamB.append(idx)
    divider(idx+1, teamA, teamB)
    teamB.pop()

N = int(input())
population = list(map(int, input().split()))
graph = [[0 for _ in range(N)] for _ in range(N)]
res = 2**31
cnt = 0
for village in range(N):
    node_list = list(map(int, input().split()))
    if node_list[0] == 0:
        continue
    else:
        for node in range(1, node_list[0]+1):
            graph[village][node_list[node]-1] = graph[node_list[node]-1][village] = 1

divider(0, [], [])
if res == 2**31:
    print(-1)
else:
    print(res)
