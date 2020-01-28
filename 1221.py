#1221. [S/W 문제해결 기본] 5일차 - GNS(어마무시한 시간, 최적화 도전해볼것)
num_decode = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}
num_encode = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}

T = int(input())

for test_case in range(1, T+1):
    a = input()
    str_list = list(input().split())
    for i in range(len(str_list)):
        str_list[i] = num_encode[str_list[i]]
    str_list.sort()
    for i in range(len(str_list)):
        str_list[i] = num_decode[str_list[i]]
    print(f'#{test_case}')
    for i in range(len(str_list)):
        print(str_list[i], end = ' ')
        