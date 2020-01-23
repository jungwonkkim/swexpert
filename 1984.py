#1984 중간 평균값 구하기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    num_list.sort()
    sum = 0
    for i in range(1, len(num_list)-1):
        sum += num_list[i]
    avg = int(round(sum/8,0))
    print(f'#{test_case} {avg}') 
