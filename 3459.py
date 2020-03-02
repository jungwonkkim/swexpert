#3459. 승자 예측하기
result = []
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnt = 0
    a = 1
    while N>0:
        N -= a
        if cnt == 0:
            a *= 4
            cnt = 1
        else:
            cnt = 0
    if cnt:
        result.append('#{} Bob'.format(test_case))
    else:
        result.append('#{} Alice'.format(test_case))

print('\n'.join(result))