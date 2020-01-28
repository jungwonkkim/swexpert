#5789. 현주의 상자 바꾸기

T = int(input())

for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    box_list = [0]*n
    for i in range(q):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            box_list[j] = i+1
    print(f'#{test_case}', end = ' ')
    for i in range(n):
        print(box_list[i], end = ' ')
    print()