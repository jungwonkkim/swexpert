#1859 백만장자


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    revenue =0
    price_list = input().split()
    price_list = [int(price) for price in price_list]
    while price_list!=[]:
        max_price = max(price_list)
        if max_price == price_list[0]:
            price_list.pop(0)
        else:
            b= price_list.index(max_price)
            for price in price_list[:b]:
                revenue += max_price - price
            del price_list[:b+1]
    print(f'#{test_case} {revenue}')
