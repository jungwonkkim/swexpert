#code created by jungwonkkim
#1215 워드퍼즐 내에 회문 찾기
def is_palindrome(string):
    rev = string[::-1]
    if rev != string:
        return False
    else:
        return True


for test_case in range(1,11):
    n = int(input())
    word_list = [list(input()) for _ in range(8)]
    word_column = [[0 for _ in range(8)] for _ in range(8)]
    word_count = 0
    for i in range(8):
        for j in range(8):
            word_column[i][j] = word_list[j][i]
    for i in range(8):
        for j in range(9-n):
            if is_palindrome(word_list[i][j:j+n]):
                word_count +=1
    for i in range(8):
        for j in range(9-n):
            if is_palindrome(word_column[i][j:j+n]):
                word_count+=1
    print(f'#{test_case} {word_count}')      