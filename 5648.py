#5648. [모의 SW 역량테스트] 원자 소멸 시뮬레이션
delta = [(0,0.5),(0,-0.5),(-0.5,0),(0.5,0)]
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    atoms = [0 for _ in range(N)]
    exploded = [False for _ in range(N)]
    res = 0
    for i in range(N):
        atoms[i] = list(map(int, input().split()))
    while True:
        if exploded.count(False)<=1:
            break
        move_res = {}
        move_cnt = {}
        for idx, atom in enumerate(atoms):
            if exploded[idx]:
                continue
            atom[0] = atom[0] + delta[atom[2]][0]
            atom[1] = atom[1] + delta[atom[2]][1]
            if -1000<=atom[0]<=1000 and -1000<=atom[1]<=1000:
                if (atom[0],atom[1]) in move_res:
                    move_cnt[(atom[0], atom[1])] +=1
                    move_res[(atom[0], atom[1])] += atom[3]
                else:
                    move_cnt[(atom[0], atom[1])] = 1
                    move_res[(atom[0], atom[1])] = atom[3]
            else:
                exploded[idx] = True
        for key in move_cnt:
            if move_cnt[key]>1:
                for idx, atom in enumerate(atoms):
                    if atom[0] == key[0] and atom[1]== key[1]:
                        exploded[idx] = True
                res += move_res[key]
    print('#{} {}'.format(test_case, res))