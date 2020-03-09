#5644. [모의 SW 역량테스트] 무선 충전
delta = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]
def max_charged(arr1, arr2):
    max_a = -1
    max_b = -1
    if arr1:
        max_a = arr1[0]
        for af in arr1:
            if charger[af][3] > charger[max_a][3]:
                max_a = af
    if arr2:
        max_b = arr2[0]
        for af in arr2:
            if charger[af][3] > charger[max_b][3]:
                max_b = af
    if max_a == max_b == -1:
        return 0
    if max_a == -1:
        return charger[max_b][3]
    if max_b == -1:
        return charger[max_a][3]
    if max_a != max_b:
        return charger[max_a][3] + charger[max_b][3]
    if len(arr1) == len(arr2) == 1:
        return charger[max_a][3]
    else:
        newarr1 = [a1 for a1 in arr1 if a1 != max_a]
        newarr2 = [a2 for a2 in arr2 if a2 != max_b]
        max__a = -1
        max__b = -1
        if newarr1:
            max__a = newarr1[0]
            for aaf in newarr1:
                if charger[aaf][3]> charger[max__a][3]:
                    max__a = aaf
        if newarr2:
            max__b = newarr2[0]
            for aaf in newarr2:
                if charger[aaf][3]> charger[max__b][3]:
                    max__b = aaf
        if max__a == -1:
            return charger[max_a][3] + charger[max__b][3]
        if max__b == -1:
            return charger[max_b][3] + charger[max__a][3]
        else:
            return max(charger[max_a][3] + charger[max__b][3], charger[max_b][3] + charger[max__a][3])


def charge(time):
    global user1
    global user2
    global charged
    if time == M:
        return
    if time == 0:
        affected1 = []
        affected2 = []
        for idx, char in enumerate(charger):
            if abs(char[1] - 1 - user1[0]) + abs(char[0] - 1 - user1[1]) <= char[2]:
                affected1.append(idx)
            if abs(char[1] - 1 - user2[0]) + abs(char[0] - 1 - user2[1]) <= char[2]:
                affected2.append(idx)
        charged += max_charged(affected1, affected2)
    affected1 = []
    affected2 = []
    user1 = [user1[0] + delta[move[0][time]][0] , user1[1] + delta[move[0][time]][1]]
    user2 = [user2[0] + delta[move[1][time]][0] , user2[1] + delta[move[1][time]][1]]
    for idx, char in enumerate(charger):
        if abs(char[1]-1-user1[0]) + abs(char[0]-1-user1[1]) <= char[2]:
            affected1.append(idx)
        if abs(char[1]-1-user2[0]) + abs(char[0]-1-user2[1]) <= char[2]:
            affected2.append(idx)
    charged += max_charged(affected1, affected2)

    return charge(time+1)



T = int(input())
for test_case in range(1, T+1):
    M, A = map(int, input().split())
    move = [list(map(int, input().split())) for _ in range(2)]
    charger = [list(map(int, input().split())) for _ in range(A)]
    user1 = [0,0]
    user2 = [9,9]
    charged = 0
    charge(0)
    print('#{} {}'.format(test_case, charged))