#1974. 스도쿠 검증

def check_sudoku(num_list):
    num_set = set(num_list)
    if len(num_set) ==9:
        return True
    else:
        return False


T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end = ' ')
    garo_list = [[0 for _ in range(9)] for _ in range(9)]
    sero_list = [[0 for _ in range(9)] for _ in range(9)]
    mangham_list= []
    for i in range(9):
        num_list = list(map(int, input().split()))
        if check_sudoku(num_list) ==False:
            mangham_list=[0]
        for j in range(9):
            garo_list[i][j] = num_list[j]   	        
    for i in range(9):
        for j in range(9):
            sero_list[i][j] = garo_list[j][i]
        if check_sudoku(sero_list[i]) ==False:
            mangham_list=[0]
    b = 0
    while(b<9):
        a = 0
        while(a<9):
            nemo_list = []
            for i in range(a, a+3):
                    for j in range(b,b+3):
                        nemo_list.append(garo_list[i][j])
            if check_sudoku(nemo_list) ==False:
                mangham_list=[0]
            a+=3
        b+=3    
    if mangham_list ==[]:
        print(1)
    else:
        print(0)