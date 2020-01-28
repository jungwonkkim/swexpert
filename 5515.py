#5515. 2016년 요일 맞추기

prev_list = [3, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

T = int(input())

for test_case in range(1, T + 1):
    month, date = map(int, input().split())
    for i in range(month):
        date+=prev_list[i]
    print(f'#{test_case} {date%7}')
