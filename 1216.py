#1216. S/W 문제해결 기본 3일차 - 회문2


def ispalindrome(str_list):
    if len(str_list)==1:
        return True
    else:
        for i in range(len(str_list)):
            if str_list[i] != str_list[-i-1]:
                return False
        return True

for test_case in range(1, 11):
    n = int(input())
    word_row = [[0 for _ in range(100)] for _ in range(100)]
    word_column = [[0 for _ in range(100)] for _ in range(100)]
    palindrome = 0
    for i in range(100):
        word_row[i] = list(input())
    for i in range(100):
        for j in range(100):
            word_column[i][j] = word_row[j][i]
    for i in range(100,0,-1):
        if palindrome == i+1:
                break
        else:
            for j in range(100):
                for k in range(101-i):
                    if ispalindrome(word_row[j][k:k + i]):
                        palindrome = i
                    else : 
                        if ispalindrome(word_column[j][k:k + i]):
                            palindrome = i
    print(f'#{n} {palindrome}')