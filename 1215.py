#1215 워드퍼즐 내에 회문 찾기

for test_case in range(1,11):
    n = int(input())
    word_list = [[0 for _ in range(8)] for _ in range(8)]
    word_column = [[0 for _ in range(8)] for _ in range(8)]
    word_count = 0
    word_reverse=[]
    for i in range(8):
        str_list = list(input())
        for j in range(8):
            word_list[i][j] = str_list[j]
    for i in range(8):
        for j in range(8):
            word_column[i][j] = word_list[j][i]
    for i in range(8):
        for j in range(9-n):
            word_reverse = word_list[i][j:j+n]
            word_reverse.reverse()
            if word_list[i][j:j+n] == word_reverse:
                word_count+=1
    for i in range(8):
        for j in range(9-n):
            word_reverse = word_column[i][j:j+n]
            word_reverse.reverse()
            if word_column[i][j:j+n] ==word_reverse:
                word_count+=1
    print(f'#{test_case} {word_count}')      