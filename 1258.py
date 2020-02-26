#1258. [S/W 문제해결 응용] 7일차 - 행렬찾기
def search(a, b):
    global matrix_list
    x = a
    y = b
    while storage[x][b] != 0:
        x+=1
    while storage[a][y] != 0:
        y+=1
    for i in range(a, x):
        for j in range(b, y):
            storage[i][j] = 0
    if matrix_list == []:
        matrix_list.append((x-a, y-b))
    else:
        for idx in range(len(matrix_list)):
            if matrix_list[idx][0] * matrix_list[idx][1]  < (x-a) * (y-b):
                if idx == len(matrix_list) - 1:
                    matrix_list.append((x-a, y-b))
                    break
                else:
                    continue
            elif matrix_list[idx][0] * matrix_list[idx][1] == (x-a)*(y-b):
                if x-a < matrix_list[idx][0]:
                    matrix_list.insert(idx, (x-a,y-b))
                    break
                else:
                    continue
            else:
                matrix_list.insert(idx, (x-a, y-b))
                break



T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    storage = [list(map(int, input().split())) for _ in range(n)]
    matrix_list = []
    for c in range(n):
        for r in range(n):
            if storage[c][r]:
                search(c, r)
    print('#{} {}'.format(test_case, len(matrix_list)), end = ' ')
    for tu in matrix_list:
        print('{} {}'.format(tu[0], tu[1]), end = ' ')
    print()