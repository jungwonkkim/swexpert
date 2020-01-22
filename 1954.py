#1954 달팽이 문제


def nail(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    if n == 1:
        matrix[0][0]=1
    elif n == 2:
        matrix[0][0] =1
        matrix[0][1]=2
        matrix[1][1]=3
        matrix[1][0]=4
    else:
        prev_matrix = nail(n-2)
        for i in range(n-2):
            for j in range(n-2):
                matrix[i+1][j+1] = prev_matrix[i][j]+4*n-4
        for i in range(n):
            matrix[0][i] = i+1
        for i in range(n):
            matrix[i][n-1] = n+i
        for i in range(n):
            matrix[n-1][i] = (3*n)-2-i
        for i in range(1,n-1):
            matrix[i][0] = (4*n)-3-i
    return matrix


T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    print(f'#{test_case}')
    nail_matrix = nail(num)
    for i in range(num):
        for j in nail_matrix[i]:
            print(j, end=' ')
        print()
    

