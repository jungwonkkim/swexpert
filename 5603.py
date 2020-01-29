#5603. [Professional] 건초더미

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    hay_list = [0]*n
    sum_r = 0
    move = 0
    for i in range(n):
        hay_list[i] = int(input())
    for i in range(n):
        sum_r += hay_list[i]
    sum_r = int(sum_r/n)
    for i in range(n):
        if hay_list[i]>sum_r:
            move += (hay_list[i]-sum_r)
    print(f'#{test_case} {move}')
