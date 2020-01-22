#1979 워드퍼즐

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    word_list = []
    word_count = 0
    for i in range(n):
        word_line = input().split()
        word_list.append(word_line)
    for i in range(n-k):
        for j in range(n-k+1):
            if word_list[i][j] =='1':
                if word_list[i][j:j+k].count('1') ==k:
                    if word_list[i][j+k] == '0':
                        word_count+=1
                        j = j+k+1
    for i in range(n-k):
        for j in range(n-k+1):
            if word_list[j][i] =='1':
                if word_list[j:j+k][i].count('1') ==k:
                    if word_list[j+k][i] == '0':
                        word_count+=1
                        j = j+k+1               
    print(word_count)