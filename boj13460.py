#13460. 구슬 탈출2

def evacuation(command, ball):
    global hole_flag
    for i in range(N):
        for j in range(M):
            if field[i][j] == ball:
                x = i
                y = j
                break
    delta = [(0,1),(0,-1),(1,0),(-1,0)]
    hole_flag = False
    if command == 'right':
        while x+delta[0][0]>-1 and x+delta[0][0]<N and y+delta[0][1]>-1 and y+delta[0][1]<M:
            nextx = x + delta[0][0]
            nexty = y + delta[0][1]
            if field[nextx][nexty] == '.':
                continue
            elif field[nextx][nexty] == 'o':
                hole_flag = True
                break
            else:
                nextx = x - delta[0][0]
                nexty = y - delta[0][1]
                break
    if command == 'left':
        while x + delta[1][0] > -1 and x + delta[1][0] < N and y + delta[1][1] > -1 and y + delta[1][1] < M:
            nextx = x + delta[1][0]
            nexty = y + delta[1][1]
            if field[nextx][nexty] == '.':
                continue
            elif field[nextx][nexty] == 'o':
                hole_flag = True
                break
            else:
                nextx = x - delta[1][0]
                nexty = y - delta[1][1]
                break
    if command == 'up':
        while x + delta[2][0] > -1 and x + delta[2][0] < N and y + delta[2][1] > -1 and y + delta[2][1] < M:
            nextx = x + delta[2][0]
            nexty = y + delta[2][1]
            if field[nextx][nexty] == '.':
                continue
            elif field[nextx][nexty] == 'o':
                hole_flag = True
                break
            else:
                nextx = x - delta[2][0]
                nexty = y - delta[2][1]
                break
        if command == 'down':
            while x + delta[3][0] > -1 and x + delta[3][0] < N and y + delta[3][1] > -1 and y + delta[3][1] < M:
                nextx = x + delta[3][0]
                nexty = y + delta[3][1]
                if field[nextx][nexty] == '.':
                    continue
                elif field[nextx][nexty] == 'o':
                    hole_flag = True
                    break
                else:
                    nextx = x - delta[3][0]
                    nexty = y - delta[3][1]
                    break
    if hole_flag == False:
        if x!=nextx or y != nexty:
            field[x][y] = '.'
            field[nextx][nexty] = ball



def plausibility(cmd):
    for i in range(N):
        for j in range(M):
            if field[i][j] == 'R':
                redx = i
                redy = j
            if field[i][j] == 'B':
                bluex = i
                bluey = j
    if cmd == 'right':
        if redx >bluex:
            evacuation('right', 'R')
            if hole_flag == False:
                evacuation('right', 'B')
        else:
            evacuation('right', 'B')
            if hole_flag == True:
                return False
            else:
                evacuation ('right', 'R')
    if cmd == 'left':
        if redx >bluex:
            evacuation('right', 'R')
            if hole_flag == False:
                evacuation('right', 'B')
        else:
            evacuation('right', 'B')
            if hole_flag == True:
                return False
            else:
                evacuation ('right', 'R')
    if cmd == 'up':
        if redx >bluex:
            evacuation('right', 'R')
            if hole_flag == False:
                evacuation('right', 'B')
        else:
            evacuation('right', 'B')
            if hole_flag == True:
                return False
            else:
                evacuation ('right', 'R')
    if cmd == 'down':
        if redx >bluex:
            evacuation('right', 'R')
            if hole_flag == False:
                evacuation('right', 'B')
        else:
            evacuation('right', 'B')
            if hole_flag == True:
                return False
            else:
                evacuation ('right', 'R')

def bfs(x):
    visit = {}
    queue = list()
    queue.append(command_seq)
    while queue :
        node = queue.pop(0)
    if node not in visit:
        visit.append(node)
        queue.extend(graph[node])



if len(command_seq)>10:
    break

elif hole_flag == True:
    break






command_list = ['right', 'left', 'up', 'down']

N, M = map(int, input().split())
field = [[] for _ in range(N)]
min_val = 11
successful = []

for i in range(N):
    field[i] = list(input())



for success in successful:
    if len(success)<min_val :
        min-val = len(success)

if min_val ==11:
    result = -1
else:
    result = min_val
print('{}'.format(result))