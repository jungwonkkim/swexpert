# 1213. [S/W 문제해결 기본] 3일차 - String 

for test_case in range(1,11):
    n = int(input())
    my_str = input()
    long_str = input()
    counter = long_str.count(my_str)
    print(f'#{n} {counter}')