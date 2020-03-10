#2383. [모의 SW 역량테스트] 점심 식사시간
def timer(arr, tuple):
    if len(arr) == 0:
        return 0
    if len(arr) <=3:
        new_arr = [abs(ele[0]-tuple[0]) + abs(ele[1]-tuple[1]) for ele in arr]
        return max(new_arr)+room[tuple[0]][tuple[1]]+1
    new_arr = sorted([abs(ele[0]-tuple[0]) + abs(ele[1]-tuple[1]) for ele in arr])
    for i in range(3, len(new_arr)):
        new_arr[i] = max(new_arr[i-3] + room[tuple[0]][tuple[1]] +1, new_arr[i]+1)
    return new_arr[-1]+room[tuple[0]][tuple[1]]


def timing(arr1, arr2):
    return max(timer(arr1, stair[0]), timer(arr2, stair[1]))

def divider (idx, team_A, team_B):
    global min_time
    if idx == len(human):
        if min_time > timing(team_A, team_B):
            min_time = timing(team_A, team_B)
        return
    team_A.append(human[idx])
    divider(idx+1, team_A, team_B)
    team_A.pop()
    team_B.append(human[idx])
    divider(idx+1, team_A, team_B)
    team_B.pop()


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    room =[list(map(int, input().split())) for _ in range(N)]
    human = []
    stair = []
    for i in range(N):
        for j in range(N):
             if room[i][j] ==1 :
                 human.append((i,j))
                 continue
             if room[i][j] >1:
                 stair.append((i,j))
                 continue
    min_time = 10000
    divider(0, [],[])
    print('#{} {}'.format(test_case, min_time))