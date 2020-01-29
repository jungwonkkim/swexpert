#6485. 삼성시의 버스 노선

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    ai_list = [0] * n
    bi_list = [0] * n
    for i in range(n):
        a, b = map(int, input().split())
        ai_list[i] = a
        bi_list[i] = b
    p = int(input())
    counter = [0] * p
    for i in range(p):
        counted = 0
        st = int(input())
        for j in range(n):
            if st >= ai_list[j] and st<=bi_list[j]:
                counted+=1
        counter[i] = counted
    print(f'#{test_case}', end = ' ')
    for i in range(p):
        print(counter[i], end = ' ')
    print()