#4406. 모음이 보이지 않는 사람


vowels = ['a','e','i','o','u']
T = int(input())

for test_case in range(1, T + 1):
    word = list(input())
    word_list = [char for char in word if char not in vowels]
    print(f'#{test_case}', end = ' ')
    for char in word_list:
        print(char, end='')
    print()
    
