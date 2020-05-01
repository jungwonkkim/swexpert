T = int(input())

for test_case in range(1, T + 1):
    num = float(input())
    ans = ''
    for i in range(1, 13):
        if num == 0:
            break
        div = 2**(-i)
        if num >= div:
            num = num - div
            ans += '1'
        else:
            ans += '0'
    if num:
        ans = 'overflow'
    print('#{} {}'.format(test_case, ans))