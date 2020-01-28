#4676. 늘어지는 소리 만들기

T = int(input())

for test_case in range(1, T + 1):
    word_list = list(input())
    N = int(input())
    hyp_list = list(map(int,input().split()))
    for hyp in hyp_list:
        if hyp == len(word_list):
            word_list[-1] = word_list[-1] + '-'
        else:
            word_list[hyp] ='-'+word_list[hyp]
    print(f'#{test_case}', end = ' ')
    for i in range(len(word_list)):
        print(word_list[i], end = '')
    print()
    
