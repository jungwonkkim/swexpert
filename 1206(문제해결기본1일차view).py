#1206. 문제해결 기본 1일차. View

for test_case in range(1, 11):
    n = int(input())
    count = 0
    apart = list(map(int, input().split()))
    compare_list = [0]*5
    for i in range(2, n-2):
        if apart[i] ==max(apart[i-2:i+3]):
            compare_list = apart[i-2:i+3]
            compare_list.sort()
            count+= compare_list[-1] - compare_list[-2]
    print(f'#{test_case} {count}')
        