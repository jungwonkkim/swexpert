#4050. 재관이의 대량 할인

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    price_list = list(map(int, input().split()))
    price_list.sort(reverse=True)
    total = 0
    for idx,p in enumerate(price_list):
        if idx%3 != 2:
            total += p
    print('#{} {}'.format(test_case, total))
