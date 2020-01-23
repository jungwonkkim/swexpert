#1979 워드퍼즐

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    word_list = [[0 for _ in range(n)] for _ in range(n)]
    word_column = [[0 for _ in range(n)] for _ in range(n)]
    word_count = 0
    one_count = 0
    for i in range(n):
        word_line = list(map(int,input().split()))
        for j in range(n):
            word_list[i][j] = word_line[j]
    for i in range(n):
        for j in range(n):
            word_column[i][j]=word_list[j][i]
    for i in range(n):
        if one_count == k:
            word_count +=1
            one_count = 0
        else:
            one_count = 0
        for j in range(n):
            if word_list[i][j] ==1:
                one_count +=1
            else:
                if one_count == k:
                    word_count+=1
                    one_count = 0
                else:
                    one_count = 0
    for i in range(n):
        if one_count == k:
            word_count +=1
            one_count = 0
        else:
            one_count = 0
        for j in range(n):
            if i==j==n-1:
                if word_column[i][j] ==1 and one_count == k-1:
                    word_count+=1
            if word_column[i][j] ==1:
                one_count +=1
            else:
                if one_count == k:
                    word_count+=1
                    one_count = 0
                else:
                    one_count = 0
    print(f'#{test_case} {word_count}')