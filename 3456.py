#3456. 직사각형 길이 찾기

T = int(input())

for test_case in range(1, T + 1):
    side_list = list(map(int, input().split()))
    result = 0
    a = side_list[0]
    if side_list.count(a) == 2:
        side_list.remove(a)
        side_list.remove(a)
        result = side_list[0]
    else:
        result = a
    print(f'#{test_case} {result}')
        
    